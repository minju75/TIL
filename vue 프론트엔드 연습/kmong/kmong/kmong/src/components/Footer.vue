<template>
    <v-row>
        <v-spacer></v-spacer>
        <div style="width: 440px; height:309.4px; padding:50px;">
            <div class="title">
                (주) 크몽 사업자 정보
            </div>     
            <ul class="margin-top-20 left-side-contents">
                <li class="plain">
                    "(주)크몽"
                    <span class="v-hr">|</span>
                    "서울시 서초구 사임당로 157, 3층"
                </li>
                <li class="plain">
                    "대표 : 박현호"
                    <span class="v-hr">|</span>
                    "개인정보보호책임 : 서동진"
                </li>
                <li class="flex-left-center plain">     
                    <span>사업자 등록 번호 : 613-81-65278</span>
                    <a href="" class="btn btn-default btn-xs">사업자 정보 확인</a>
                </li>
                <li class="plain">통신판매업신고 : 2014-서울강남-01471호</li>
                <li class="plain">
                    "1544-6254"
                    <span class="v-hr">|</span>
                    "help@kmong.com"
                </li>
                <li class="plain">호스팅, 사업자 : Amazon Web Service(AWS)</li>
            </ul>       
        </div>
        <div  style="width: 800px; height:309.4px; padding: 50px;">
            <v-row>
            <div class="title">
                크몽
            <ul class="margin-top-20 right-side-contents">
                <li class="plain">
                    마켓
                </li>
                <li class="plain">
                    마켓 prime
                </li>
                <li class="plain">
                    맞춤견적
                </li>
                <li class="plain">
                    엔터프라이즈
                </li>
                <li class="plain">
                    쑨 soon
                </li>
            </ul>
            </div>          
            <div class="title" style="width: 140px; height:309.4px;">
                크몽 정보
            <ul class="margin-top-20 right-side-contents">
                    <li class="plain">서비스소개</li>
                    <li class="plain">인재영입</li>
                    <li class="plain">크몽 PRESS</li>
            </ul>
            </div>                
            <div class="title" style="width: 140px; height:309.4px;">
                관련사이트
            <ul class="margin-top-20 right-side-contents">
                    <li class="plain">크몽블로그</li>
                    <li class="plain">크몽유튜브</li>
                    <li class="plain">크몽인스타그램</li>
                    <li class="plain">크몽 기술 블로그</li>
            </ul>
            </div>                
            <div class="title" style="width: 140px; height:245.8px;">
                고객센터
            <ul class="margin-top-20 right-side-contents">
                <li class="plain">공지사항</li>
                <li class="plain">FAQ</li>
                <li class="plain">이용약관</li>
                <li class="plain">개인정보처리방침</li>
                <li class="plain">전문가 센터</li>
                <li class="plain">1 : 1 문의</li>
            </ul>
            <hr>
            <div style="width: 240px; height:51.2px;">               
                <div class="title">
                    운영시간
                </div>
                <p class="plain">평일 10:30 ~ 18:30</p>
            </div>
           </div>
            
        
        </v-row>
        
        </div>
    <v-spacer></v-spacer>    
    </v-row>
</template>

<script>
  export default {
    name: 'Footer',
    components: {

    }
  }
</script>

<style>
    .title{
        font-weight: 500;
        font-size: 14px;
        color: #333;
        line-height: 2.35;
        width: 140px;
        height: 32.8px;
    }
    .plain{
        color: #666;
        cursor: pointer;
    }
</style>