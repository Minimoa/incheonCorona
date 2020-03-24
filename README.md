# 인천 코로나 맵
[울산 코로나맵](https://coronamap-ulsan.site/) 개발진들이 [**각 지역의 코로나맵 제작**을 좀 더 쉽고 빠르게 제작할 수 있도록 배포한 Django APP](https://github.com/nero96in/coronamap_deploy/)을 이용하여 제작하였습니다. 

### 사용한 API
1. [공공 데이터 포털 공적 마스크 판매 현황 API](https://app.swaggerhub.com/apis-docs/Promptech/public-mask-info/20200307-oas3#/)
2. [Kakao map API](http://apis.map.kakao.com/)

### 개발진
- **[이정인](https://alreadyusedadress.tistory.com/)(인하대 컴퓨터공학과)  
- 기타 문의: alslahdk@likelion.com

---

### 목차
1. [기능 설명](#기능-설명) 
	
---
# 기능 설명
#### 모바일과 데스크탑 화면 모두 호환되어있는 깔끔한 UI의 지역 단위 코로나맵입니다. 세부 기능은 아래와 같습니다.

1. 지역 내 공적 마스크 판매처와 현황을 마커로 표시해 줍니다.  
<img width="720" alt="mask-stores" src="https://user-images.githubusercontent.com/49309450/77252324-75794f00-6c96-11ea-82b2-c416455c3a5e.png">  

2. 30일 내에 확진자가 다녀간 동선을 주황색 마커로 표시해 줍니다. 다녀간 지 오래될 수록 색이 옅어집니다.  
<img width="720" alt="patients" src="https://user-images.githubusercontent.com/49309450/77252328-7b6f3000-6c96-11ea-9eba-15c120146062.png">  

3. 공적 마스크 판매처와 현황, 확진자 정보, 확진자 동선 정보 등을 주기적으로 **자동 업데이트**하고 확진자 동선이 업데이트될 시 **메일**로 수신 가능합니다.  

4. 지역 내 선별 진료소를 표시해줍니다.  
<img width="720" alt="hospitals" src="https://user-images.githubusercontent.com/49309450/77252331-7d38f380-6c96-11ea-91a6-2b2f4ffd6eb9.png">  

5. 확진자 동선을 GUI로 쉽고 빠르게 추가할 수 있습니다.  
<img width="720" alt="patient-admin" src="https://user-images.githubusercontent.com/49309450/77252326-79a56c80-6c96-11ea-87e3-e1108a22a4e2.png">  

---

## 이슈 
 -인천 선별 진료소의 모든 데이터를 카카오맵에서 자체적으로 가져오지 못하는 것 같음 따로 크롤링 하여 추가할 예정
