<template>
    <header class="body">
        <div>
            <v-img alt="banner" src="@/assets/kmong_awards_banner_4.jpg"></v-img>
        </div>
        <hr>
        <v-container color="#FFEB3B">
        <div class="headerBox">       
            <v-row color="#FFEB3B">
                <li><img 
                alt="logo" 
                src="@/assets/kmong_logo.png" 
                style="width: 106px; height: 80px;"
                /></li>
                <v-spacer></v-spacer>
                    <li class="center" style="width: 68.04px; height: 22.4px;"><span style="color: #F44336;">마켓 prime</span></li><br>
                    <li class="center" style="width: 65.7px; height: 21.6px;">전문가 등록</li><br>
                    <li class="center" style="width: 65px; height: 21.6px;">로그인</li><br>
                    <div style="width: 106px; height: 37.2px;">
                        <v-btn 
                        color="#1E88E5"
                        class="font-color-fff"
                        >
                        무료 회원가입
                        </v-btn>
                    </div>
            </v-row>  
        </div>
        </v-container>
        <v-space></v-space>
        <div class="margin-top-15">
            <v-space></v-space>
            <div class="center">
                <v-spacer></v-spacer>
                <p style="height: 26px;">186만건의 거래, 98.4%의 만족도</p>
                <v-spacer></v-spacer>
                <h1 class="font-weight-black" style="height: 44.8px;">프리랜서 마켓, 크몽</h1>
                <v-spacer></v-spacer>
                <div class="SearchForm search-form" style="margin 0 auto;">
                    <input type="text" class="white center" style="width: 650px; height: 70px;" placeholder="웹사이트 개발">
                    <!-- <v-text-field
                        hide-details
                        prepend-icon="mdi-magnify"
                        single-line>
                    </v-text-field> -->
                </div>
                <p></p>
            </div>
        </div>
        <div class="center">
            <v-spacer></v-spacer>
            <div class="white-border"></div>
                <p class="header container margin: auto">또는</p>
            <v-spacer></v-spacer>
            <div class="underline">
                기업고객 맞춤 서비스 이용하기>
            </div>
        </div>
        <div>
            <div style="margin-right: auto; margin-left: auto; width: 1300px;">
                <div class="RootDirectoryTheme" style="height: 50px;">
                    <br>
                    <v-row>
                        <v-spacer></v-spacer>
                        <div>
                            <a href="">디자인</a>
                        </div>
                        <v-spacer></v-spacer>              
                        <div>
                            <a href="">IT/프로그래밍</a>
                        </div>
                        <v-spacer></v-spacer>
                        <div>
                            <a href="">영상/사진/음향</a>
                        </div>
                        <v-spacer></v-spacer>
                        <div>
                            <a href="">마케팅</a>
                        </div>
                        <v-spacer></v-spacer>
                        <div>
                            <a href="">번역/통역</a>
                        </div>
                        <v-spacer></v-spacer>
                        <div>
                            <a href="">문서/글쓰기</a>
                        </div>
                        <v-spacer></v-spacer>
                        <div>
                            <a href="">비즈니스 컨설팅</a>
                        </div>
                        <v-spacer></v-spacer>
                        <div>
                            <a href="">취업/투잡</a>
                        </div>
                        <v-spacer></v-spacer>
                        <div>
                            <a href="">운세/상담</a>
                        </div>
                        <v-spacer></v-spacer>
                        <div>
                            <a href="">레슨/실무교육</a>
                        </div>
                        <v-spacer></v-spacer>
                        <div>
                            <a href="">주문제작</a>
                        </div>
                        <v-spacer></v-spacer>
                    </v-row>
                </div>
            </div>
        </div>
    </header>
</template>


<script>
  export default {
    name: 'Header',
    components: {

    },
  }
</script>
<style>
    .body{
        background-color: #FFF176;
    }
    .headerBox{width:1170px; margin:0 auto;}
    .underline:hover {
        border-bottom:1px solid  black;
    }
    .center{
        text-align: center;
    }
    .white{
        background-color: white;
    }
    .RootDirectoryTheme{
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
        word-break: break-all;
        background-color: white;
        border-top-left-radius: 50px;
        border-top-right-radius: 50px;
        line-height: 1.8;
    }
    
</style>