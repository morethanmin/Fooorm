# fooorm

> google forms와 유사한 설문지 유형의 서비스
> Django를 공부하기 위해 만들었고, frontend는 별도의 상태관리 프레임워크를 사용하진 않았습니다.

## Live demo

you can make survey [here](http://34.64.167.215:7000/)

you can answer example survey [here](http://34.64.167.215:7000/forms/p6rRECBjzrrReNJ4XSdF)

test user : (id: mini4614, pw: asd123)

## Preview

![chrome-capture](https://user-images.githubusercontent.com/72514247/129503204-83f947a7-4ce9-4e08-973d-7964ec5fd6d8.gif)

## Features

- 설문지 생성
- 질문 생성 (택스트, 객관식, 체크박스)
- 설문지 공유
- 응답 결과 확인 (요약, 질문, 개별보기)
- 응답 결과 .csv형식 다운로드

## 개발할 기능

- 설문지 검색

## Tech and libraries

- django 3.2.6
- jquery
- sqlite 3.36.0
- toastr
- jquery.cookie
- chart.js

## Getting started

- use git clone.

```bash
$ git clone https://github.com/morethanmin/Fooorm.git
$ cd Fooorm
$ python3 manage.py runserver (or python manage.py runserver)
```

- open http://localhost:8000/

## Note

This project is ongoing.

## License

This project is licensed under the MIT License - see the LICENSE.md for details
