## 👑 팀명 : 퀸🫅 & 킹🤴 그리고 잼민이들🤦‍♂️<br>
<p align="center"><img src="./img/sk.png" width="900" height="300"/></p>

 
### 🐿️ 팀원

|오정연|이호재|변가원|이진섭|김태욱|
|:---:|:---:|:---:|:---:|:---:|
|<img src="https://github.com/user-attachments/assets/d920daaf-3baa-441d-ab1c-babb240b307b" width="140" height="140">|<img src="https://github.com/user-attachments/assets/23848016-2562-40b7-82ad-69c0edc6c8cb" width="140" height="140"> |<img src="https://github.com/user-attachments/assets/a2497f47-8214-43c4-81f3-ed3ee637bbf5" width="140" height="140"> | <img src="https://github.com/user-attachments/assets/90d30dde-dfe5-4929-938f-2941dec79d65" width="140" height="140"> | <img src="https://github.com/user-attachments/assets/60a82e31-52ef-4de3-8d52-a50037491b56" width="140" height="140"> |
|[@Jungyunn](https://github.com/Jungyunn)|[@HoJL](https://github.com/HoJL)|[@dnjsrk](https://github.com/dnjsrk)|[@jururuj](https://github.com/jururuj)|[@Taeuk-Dog](https://github.com/Taeuk-Dog)|
|**Project Leader**<br/>LLM|LLM<br>Data Debugging|Data Preprocessing<br>ReadMe|Data Preprocessing<br>Streamlit<br>ReadMe|Streamlit<br> 화면구현<br>ReadMe 작성|


</div>

<hr>

### 🎖️ 프로젝트 개요
hallucination이 없는 챗봇 시스템 구현 

<hr>

### 🎖️ 프로젝트 목표


'Enco Library Chatbot'은 'Enco Library'가 소장한 도서에 대해 검색을 했을 때 hallucination이 없는 답변을 제공하는 것을 목표로 합니다.


<hr>

### 🔨 기술 스택
<div>

_Environment_
<br><br>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white"/>
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"/>
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"/>

_Development_
<br><br>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white">
<img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white">
<img src="https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
<img src="https://img.shields.io/badge/json-000000?style=for-the-badge&logo=json&logoColor=white">


<hr> 

### Prerequisites
**이 프로젝트를 실행하기 위해 필요한 패키지 등을 정의**

```cmd
pip install -r requirements.txt, langchain을 이용하기위한 .env파일 정의
```

<hr>

### Usage
**이 코드를 실행하기 위해 어떠한 코드를 어떻게 실행해야 하는지 작성**

```cmd
streamlit run script_model.py
chrom run --path [크로마db패스]
```

<hr> 

### Data

국립중앙도서관의 Linked Open Data(LOD)에서 텍스트 기반의 일반 도서 정보 데이터셋을 이용하여 프로젝트를 진행하였습니다.
<br>
<br>
<a href='https://lod.nl.go.kr/home/dataset/datadownload.do'><img src='./img/lod.png'></a>
<br>
<br>
_data column_ 

```
title: 도서의 제목
creator: 도서의 저자
publisher: 도서의 출판사
issuedYear: 도서의 발행년도
issued: 도서의 출판년도
kdc: 도서의 한국 십진분류 코드
ddc: 도서의 듀이 십진분류 코드
alternative: 도서의 주제와 관련된 다른 도서
keyword: 도서의 키워드
seeAlso: 도서의 관련 링크
```

책 content의 경우 관련 정보가 부족하여 api를 활용하여 크롤링하였습니다.<br>
<hr>


### Preprocess

수집한 도서 데이터셋의 크기가 3700000개로 매우 방대하여 큰 파일을 70개로 나눈 후 그중 6개 파일을 선택하여 정제 후 하나로 합치고 그 파일을 24000개씩 나누어 9개의 정제된 파일을 만들었습니다.<br>

도서관에서는 책을 주제별로 숫자로 분류하여 서가에 정리합니다. 이때 사용되는 분류 체계가 KDC(한국십진분류)와 DDC(듀이 십진분류)입니다. <br>

정제 과정에서는 도서의 제목이 한글인 것으로 하도록 하였으며 KDC 코드와 DDC 코드의 앞 두 자리에 해당하는 주제를 찾아 각각 main_kdc_description과 main_ddc_description에 저장하였습니다. 또한, KDC와 DDC 코드가 모두 존재하는 경우, 국내 도서관에서 더 널리 사용되는 KDC를 기준으로 location(도서관 내 책의 위치)과 mainCategoryDescription(책의 주제)을 추출하도록 하였습니다.


<hr>

### System Architecture

<img src='./img/아키텍쳐.png'> <br>

<hr>

### 수행 결과
<img src='./img/hallucination.png'> -> 올바르지 않은 출판사 답변 제공<br><br>
<img src='./img/none_hallu.png'> -> 올바른 출판사 답변 제공<br><br>
기존의 gpt에서는 도서를 질문하였을 때 그 책에 대한 정보를 정확하게 답변해 주지 않는 hallucination 문제가 자주 발생하는 모습을 보였습니다. <br> Rag 기법을 이용하여 국립중앙도서관의 도서 정보에 관여하여 그 도서에 대한 정확한 답변을 추출할 수 있도록 하였습니다.<br><br>

<img src='./img/creator.png'>작가에 대해 검색했을 때<br><br>
<img src='./img/book.png'>책에 대해 검색했을 때<br><br>
<img src='./img/category.png'>카테고리에 대해 검색했을 때<br><br>
<img src='./img/keword.png'>키워드에 대해 검색했을 때<br><br>
<img src='./img/none.png'>enco 도서관에 없는 책을 검색했을 때<br><br>

_문제상황_ <br><br>
대용량의 데이터를 전처리하고 vectordb에 저장하기 전, 20개의 데이터로 테스트했을 때는 검색이 잘 되는 것을 확인하였지만, 이후에 중간단계를 거치지 않고 한번에 20만개 정도의 데이터를 임베딩 후 검색 실행 시 일부 케이스들에 대해서 잘 안되는 것을 확인하였습니다.<br><br>

_개선 방안_<br><br>
데이터 개수를 점진적으로 늘려가며 문제가 생기는 데이터 범위를 미리 확인했으면 좋았을 것 같습니다.<br>
현재는 기본 OpenAIEmbeddings(model='text-embedding-3-small') 를 사용하였으나, 이 임베딩이 본 데이터에 적합하지 않을 수 있다고 생각했습니다.
-> 데이터에 맞는 embedding 모델로 fine-tuning 하는 방식 적용 가능<br>
document의 형식이 metadata, page_content가 있는데 metadata 형식을 충분히 활용하지 못하였습니다.<br><br>

<hr>

### 한 줄 회고

오정연 - 데이터가 정말정말정말 중요하구나,,,
<br>
이호재 - 뀨우잉
<br>
변가원 - 모든 프로젝트는 기획 단계가 제일 중요하다,,,
<br>
이진섭 - 뀨잉
<br>
김태욱 - 뀨우우....