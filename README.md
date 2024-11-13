<p align="center"><img src="https://github.com/user-attachments/assets/631d3dde-fafd-4671-a5b7-730edd378f8a" width="900" height="300"/></p>

<hr>

### 🐰 팀명 : 퀸 & 킹 그리고 아이들
 
### 🐿️ 팀원

|오정연|이호재|변가원|이진섭|김태욱|
|:---:|:---:|:---:|:---:|:---:|
|<img src="https://github.com/user-attachments/assets/d920daaf-3baa-441d-ab1c-babb240b307b" width="140" height="140">|<img src="https://github.com/user-attachments/assets/23848016-2562-40b7-82ad-69c0edc6c8cb" width="140" height="140"> |<img src="https://github.com/user-attachments/assets/a2497f47-8214-43c4-81f3-ed3ee637bbf5" width="140" height="140"> | <img src="https://github.com/user-attachments/assets/90d30dde-dfe5-4929-938f-2941dec79d65" width="140" height="140"> | <img src="https://github.com/user-attachments/assets/60a82e31-52ef-4de3-8d52-a50037491b56" width="140" height="140"> |
|[@Jungyunn](https://github.com/Jungyunn)|[@HoJL](https://github.com/HoJL)|[@dnjsrk](https://github.com/dnjsrk)|[@jururuj](https://github.com/jururuj)|[@Taeuk-Dog](https://github.com/Taeuk-Dog)|
|**Project Leader**<br/>LLM|LLM<br>Data Debugging|Data Preprocessing|Data Preprocessing<br>Streamlit|Streamlit<br> 화면구현<br>ReadMe 작성|


</div>

<hr>

### 🎖️ 프로젝트 개요
  

<hr>

### 🎖️ 프로젝트 목표


'Enco Library Chatbot'은 효율적으로 한글 도서를 관리하고 사용자에게 효율적인 정보를 제공합니다!


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
<img src="https://img.shields.io/badge/json-000000?style=for-the-badge&logo=json&logoColor=white">



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

도서관에서는 책을 주제별로 숫자로 분류하여 서가에 정리합니다. 이때 사용되는 분류 체계가 KDC(한국십진분류)와 DDC(덱시 십진분류)입니다. 'Enco Library Chatbot'에서는 도서관 데이터 중 책의 제목, 저자, 출판사, 발행년도, KDC, DDC, 추천 도서, 키워드, 관련 링크만을 활용하도록 설정하였습니다. 데이터 양이 방대하여 책 제목이 한글로 된 도서만을 추출하기로 결정하였습니다.

추출 과정에서는 KDC 코드와 DDC 코드의 앞 두 자리에 해당하는 주제를 찾아 각각 main_kdc_description과 main_ddc_description에 저장하였습니다. 또한, KDC와 DDC 코드가 모두 존재하는 경우, 국내 도서관에서 더 널리 사용되는 KDC를 기준으로 location(도서관 내 책의 위치)과 mainCategoryDescription(책의 주제)을 추출하도록 하였습니다.


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