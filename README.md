<p align="center"><img src="https://media.discordapp.net/attachments/1305691081454649454/1305719340850614352/c0a6fccd86421520.png?ex=67340d65&is=6732bbe5&hm=9a5431854cfdf7f4eee60372626d5856be693a4ff9bb4976d9b9e819b65f69e2&=&format=webp&quality=lossless&width=921&height=526" width="900" height="300"/></p>

<hr>

### 🐰 팀명 : 퀸 & 킹 그리고 아이들
 
### 🐿️ 팀원


|오정연|이호재|변가원|이진섭|김태욱|
|:---:|:---:|:---:|:---:|:---:|
|<img src="https://media.discordapp.net/attachments/1305691081454649454/1305700535852204102/image_2.png?ex=6733fbe2&is=6732aa62&hm=d70145508766c2ce28f69d0ace552a2d23903d047a9eed4392c473c4c45a3ceb&=&format=webp&quality=lossless" width="140" height="140"/>|<img src="https://media.discordapp.net/attachments/1305691081454649454/1305701083162607696/image.png?ex=6733fc64&is=6732aae4&hm=29226d65da4111221ed0714feb928e24a4078fe2ec0c0db663d44fcfc3f772a9&=&format=webp&quality=lossless" width="140" height="140"/> |<img src="https://media.discordapp.net/attachments/1305691081454649454/1305703249923538994/image.png?ex=6733fe69&is=6732ace9&hm=86e80a5d45eac1fdf6ae13ed6ea136da67e6397661aae0f4fc69e75075786d4e&=&format=webp&quality=lossless" width="140" height="140"/> | <img src="https://media.discordapp.net/attachments/1305691081454649454/1305701990097227806/images.png?ex=6733fd3d&is=6732abbd&hm=1e5f33fe4431966ec4796a2a483b87728f5beed9ba9c0390ac540437e46e971f&=&format=webp&quality=lossless" width="140" height="140"/> | <img src="https://avatars.githubusercontent.com/u/174983658?s=400&u=5f1662f95ced679e306eeca0c47b6da33aed1f8f&v=4" width="140" height="140"/> |
|[@Jungyunn](https://github.com/Jungyunn)|[@HoJL](https://github.com/HoJL)|[@dnjsrk](https://github.com/dnjsrk)|[@jururuj](https://github.com/jururuj)|[@Taeuk-Dog](https://github.com/Taeuk-Dog)|
|**Project Leader**<br/>LLM|LLM<br>Data Debugging|Data Preprocessing|Data Preprocessing<br>Streamlit|Streamlit<br> 화면구현<br>ReadMe 작성|
 
</div>

<hr>

### 🎖️ 프로젝트 개요
  

<hr>

### 🎖️ 프로젝트 목표
도서관에서의 책은 주제별로 숫자를 분류하여 서가에 정리를 합니다.
그 숫자가 바로 kdc와 ddc입니다.
'Enco Library Chatbot'에서는 도서관 데이터에서 책의 제목, 저자, 출판사, 발행년도, kdc, ddc, 다른 책 추천, 키워드, 관련 링크 만을 이용하도록 하였습니다.
데이터의 수가 너무 많아 책 제목이 한글로 된 도서를 추출하기로 했습니다.
kdc 코드와 ddc 코드의 앞 두자리에 맞는 주제를 찾아 main_kdc_description과 main_ddc_description에 넣었으며,
kdc와 ddc가 둘다 존재하는 데이터라면 국내 도서관에서 더 많이 사용하는 kdc를 이용하여 location(도서관에서의 책 위치)과 mainCategoryDescription(책의 주제)를 추출해주도록 하였습니다.



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
<img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">



<hr>

### Prerequisites

```cmd
streamlit 1.37.1
openai 0.28.0
```

<hr>

### Usage

```cmd
streamlit run main.py
```

<hr> 

### Data

***data에 대한 설명 작성***


<hr>


### Preprocess

수집한 데이터의 크기가 매우 방대하여 큰 파일을 70개로 나눈 후 그중 6개 추출하여 진행


<hr>

### System Architecture

***프로그램의 전체적인 구성 도표 삽입 및 설명***

<hr>

### 수행 결과

***시스템 구축 전후의 결과 비교 및 평가, 한계점 기술***

<hr>

### 한 줄 회고

오정연 - 
<br>
이호재 - 
<br>
변가원 - 
<br>
이진섭 - 
<br>
김태욱 - 