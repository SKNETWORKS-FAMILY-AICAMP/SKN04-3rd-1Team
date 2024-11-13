
from langchain_core.runnables import (
    RunnableLambda,
    ConfigurableField,
)
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    PromptTemplate,
)
from langchain_core.output_parsers import (
    StrOutputParser
)
from operator import itemgetter
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache
from langchain_community.document_transformers import LongContextReorder
from langchain_openai.embeddings import OpenAIEmbeddings
import chromadb


def reorder_documents(documents):
    # LongContextReorder 객체 생성: 긴 문맥을 재정렬하는 기능
    context_reorder = LongContextReorder()
    
    # 입력된 문서들을 재정렬
    documents_reordered = context_reorder.transform_documents(documents)
    
    # 재정렬된 문서의 내용을 줄바꿈으로 구분하여 하나의 문자열로 결합
    documents_joined = '\n'.join([document.page_content for document in documents_reordered])

    return documents_joined  # 재정렬된 문서의 내용을 반환


load_dotenv()
set_llm_cache(InMemoryCache())

client = chromadb.HttpClient(host='192.168.0.10', port=8000)
# collection = client.get_collection('books')
chroma_db = Chroma(collection_name='books', client=client, embedding_function=OpenAIEmbeddings(model='text-embedding-3-small', show_progress_bar=True))
ret =  chroma_db.as_retriever(
    search_kwargs={'k': 5},    
).configurable_fields(
    # 검색 알고리즘을 선택할 수 있는 필드 설정
    search_type=ConfigurableField(
        id='search_type',  # 필드의 고유 ID
        name='Search Type',  # 사용자에게 보여질 필드 이름
        description='검색 알고리즘 선택'  # 필드에 대한 설명
    ),
    # 검색 알고리즘의 설정을 위한 필드 설정
    search_kwargs=ConfigurableField(
        id='search_kwargs',  # 필드의 고유 ID
        name='Search Kwargs',  # 사용자에게 보여질 필드 이름
        description='검색 알고리즘의 config'  # 필드에 대한 설명
    )
)

# 프롬프트 템플릿 정의: reference, question, language를 포함
template = '''
주어진 reference를 최대한 활용하라 
아래항목을 참고해
title항목은 책 제목, creator항목은 작가, alternative항목은 부제목(원제목) location항목은 도서관 섹션, issued항목은 발행, content항목은 책 소개
여기서 title항목에서 책제목검색을 creator항목에서 작가검색을 alternative에서 부제목검색을 content에서 책소개를 검색하는거야
{reference}

다음 질문에 답하라,
작가나 사람이름이나 작품에 대한 질문을할때는 creator항목을 보고 찾아줘
책제목을 질문할때는 title항목을 참고하여 찾아줘
책내용을 질문할때는 content항목을 참고하여 찾아줘
결과를 내놓을때 location항목도 넣어줘
여러개의 작품을 추천할때 없는정보는 빼줘:
{question}
'''

# 템플릿으로부터 프롬프트 생성
prompt = PromptTemplate.from_template(template)

# OpenAI의 Chat 모델 초기화 (gpt-4o-mini 모델 사용)
model = ChatOpenAI(model_name='gpt-4o-mini')

# 출력 파서를 초기화 (문자열 출력을 처리)
parser = StrOutputParser()

# 체인 구성: 데이터 흐름을 정의
chain = (
    {
        # 'reference' 키에 대해 여러 처리를 정의
        'reference': itemgetter('question')  # 질문에서 reference를 추출
        | ret  # Chroma 리트리버로부터 데이터를 검색
        | RunnableLambda(reorder_documents),  # 문서를 재정렬
        'question': itemgetter('question'),  # 질문을 그대로 가져오기
    }
    | prompt  # 프롬프트 템플릿에 데이터 결합
    | model  # 모델에 프롬프트 전달하여 응답 생성
    | parser  # 모델의 응답을 파싱
)


def get_chain_result(query):
    response = chain.invoke({
        'question': query
    })

    return response






