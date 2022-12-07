# 한밭대학교 컴퓨터공학과 러닝피그팀

**팀 구성**
- 20191784 이성철 
- 20197118 강지훈
- 20191733 박태원

## <u>Teamate</u> Project Background
- ### 필요성
  - 돼지를 키울 때 가장 중요한 것이 집단 폐사를 막는 것인데, 그를 위해 돈사의 지속적인 관찰을 축산 산업의 특성(분뇨, 악취, 사육두수 등)때문에 사람이 직접 지속적인 내, 외부적인 환경을 관리할 수 없다
  - 돼지고기 수급 전망은 코로나 19로 인한 수요 증가로 인한 농장 당 사육 수 증가, 육류 수입량 증가 등의 요인으로 도매가격이 내려가고, 그에 따라 가격경쟁이 더욱 필요해졌다

- ### 기존 해결책의 문제점
  - 질병 등으로 인한 아픈 돼지 발생 시에 사람이 직접 개체마다 검사를 진행하거나 돈사 또는 돈칸에 있는 모든 개체에게 백신 투여를 해야하기 때문에 많은 비용이 요구된다
  - 자돈 돈사처럼 사육두수가 많은 경우 검사 시에 돈칸 내에서 놓치는 개체가 발생할 수 있다
  - 기존 선행 연구들이 실제 돈사 사육 운영, 관리등에 바로 적용할 수 있는 방안이 없음
  
  EX) 축산 ICT 장치 기준설정 및 빅데이터 활용, 젖소 건강 모니터링 기술 연구, 국가동물건강감시시스템
  
- ### 제시하는 해결책
  - 실제 돈사의 촬영한 영상데이터에서 돼지를 레이블링하여 모델에 적용
  - 학습된 모델을 통해 활동성이 저하된 돼지와 돼지의 결집 정도를 사용자(사양관리자)에게 알려주는 앱/웹
  
## System Design
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Pytorch-EE4C2C?style=flat-square&logo=Pytorch&logoColor=white"/> <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=Flutter&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white"/> <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/> 

  - ### 시스템 구성도
    ![KakaoTalk_20221205_235032828](https://user-images.githubusercontent.com/102698011/205670757-59b35e90-f7e7-4275-8a34-ceaed012c9da.png)
  - ### 객체탐지, 추적모델
  
    ![ sss111 ](https://user-images.githubusercontent.com/102698011/206099267-9a2f1c5e-adfa-43d6-9e97-5a1e0c62450e.PNG)
     ###### 이미지 출처:<https://medium.com/@shahrullo/visual-perception-for-self-driving-cars-part-2-6be5a1ca34bd>
      - YOLOv5s와 StrongSORT를 통해 객체탐지, 추적을 진행함
  - ### 이미지     
    ![image](https://user-images.githubusercontent.com/113576261/206102140-8b87d09a-db8a-484a-9838-ddef945a6241.png)

    
## Case Study
  - ### Description
  
    - 실제 돈사에서 촬영된 돼지 영상을 활용해 약 3000장 이상의 이미지 레이블링(데이터셋 구축)
    
    ![image](https://user-images.githubusercontent.com/66303929/206100652-ae54633b-0069-4b17-8966-0f661cd4bc67.png)

    - YOLOv5와 DeepSort 학습 모델을 통해 돼지 탐지 및 추적
    - 추적한 돼지의 ID를 바탕으로 현재 프레임과 이전 프레임 비교해 움직인 거리 계산
    - ID, Distance, Time 등을 DB에 저장하고 플러터(Flutter)를 통해 웹으로 보여줌
    - API 서버를 사용해 학습한 결과를 DB에서 받아 저장 후 다시 플러터에서 받는 순서로 진행
    - 포트포워딩을 통해 각자의 서버에서 데이터 전달
    
## Conclusion
  - ### 최종 결과물
  ![ssssss2111``](https://user-images.githubusercontent.com/102698011/205670279-c93ad452-94ea-4941-b2d5-866da4b4e432.PNG)

  
  
  - ### 결과물의 문제점
    - 다른 돈사에서 기존의 모델을 적용하려면 추가 라벨링이 필요
    - 객체가 사물에 가려지거나 겹치는 현상에 따른 새로운 ID할당을 받으면서 ID별로 정확한 돼지의 활동량을 검출하기 어려움
 
  - ### 문제점에 대한 대안
    - 트래킹 쪽에서 ID풀림 현상을 대체할만한 알고리즘 개발
    - 돈사에 있는 각각 돼지들의 활동량을 파악하는게 아닌 돈사의 구역별로 나누어진 곳의 활동량을 파악해 다른 구역과의 활동량 차이를 비교
