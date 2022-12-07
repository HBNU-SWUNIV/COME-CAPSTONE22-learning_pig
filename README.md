# 한밭대학교 컴퓨터공학과 러닝피그팀

**팀 구성**
- 20191784 이성철 
- 20197118 강지훈
- 20191733 박태원

## <u>Teamate</u> Project Background
- ### 필요성
  - 돼지를 키울 때 가장 중요한 것이 집단 폐사를 막는 것인데, 그를 위해 돈사의 지속적인 관찰을 축산 산업의 특성(분뇨, 악취, 사육두수 등)때문에 사람이 직접 지속적인 내, 외부적인 환경을 관리할 수 없다.
  - 돼지고기 수급 전망은 코로나 19로 인한 수요 증가로 인한 농장 당 사육 수 증가, 육류 수입량 증가 등의 요인으로 도매가격이 내려가고, 그에 따라 가격경쟁이 더욱 필요해졌다.

- ### 기존 해결책의 문제점
  - OOO
  - OOO
  
## System Design
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Pytorch-EE4C2C?style=flat-square&logo=Pytorch&logoColor=white"/> <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=Flutter&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white"/> <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/> 

  - ### System Requirements
    - 모델 도면
    
    ![KakaoTalk_20221205_235032828](https://user-images.githubusercontent.com/102698011/205670757-59b35e90-f7e7-4275-8a34-ceaed012c9da.png)
    - OOO
    
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
  - ### OOO
  ![ssssss2111``](https://user-images.githubusercontent.com/102698011/205670279-c93ad452-94ea-4941-b2d5-866da4b4e432.PNG)

  
  - ### OOO
  
