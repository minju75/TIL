<template>     
    <div>
        <div style="margin-left: auto; margin-right: auto; width: 1170px;">      
            <div style="padding: 10px;"><h3>마케팅 카테고리에서 인기있어요!</h3></div>
            
            <div style="width: 1170px; ">
                <div>
                <v-row>    
                    <v-card
                    class="category"
                    ><img src="@/assets/category-217@2x.png" alt="블로그, 카페">
                    <p class="bottomleft">블로그, 카페</p>
                    </v-card>
                    <v-card
                    class="category"
                    ><img src="@/assets/category-203@2x.png" alt="블로그, 카페">
                    <p class="bottomleft">SNS 마케팅</p>
                    </v-card>
                    <v-card
                    class="category"
                    ><img src="@/assets/category-219@2x.png" alt="블로그, 카페">
                    <p class="bottomleft">쇼핑몰/ 스토어</p>
                    </v-card>
                    <v-card
                    class="category"
                    ><img src="@/assets/category_2_236.jpg" alt="블로그, 카페">
                    <p class="bottomleft">웹트래픽</p>
                    </v-card>
                    <v-card
                    class="category"
                    ><img src="@/assets/category_2_235.jpg" alt="블로그, 카페">
                    <p class="bottomleft">체험단/기자단</p>
                    </v-card>
                    </v-row>   
                </div>                       
            </div>
            <div style="margin-left: auto; margin-right: auto; width: 1170px; height: 197.8px;">      
                <div style="padding: 10px;"><h3>디자인 카테고리에서 인기있어요!</h3></div>
                <v-spacer></v-spacer>
                <div>
                <v-row>    
                    <v-card
                    class="category"
                    ><img src="@/assets/category-101@2x.png" alt="블로그, 카페">
                    <p class="bottomleft">로고 / 브랜딩</p>
                    </v-card>
                    <v-card
                    class="category"
                    ><img src="@/assets/category-107@2x.png" alt="블로그, 카페">
                    <p class="bottomleft">인쇄/홍보물</p>
                    </v-card>
                    <v-card
                    class="category"
                    ><img src="@/assets/category-104@2x.png" alt="블로그, 카페">
                    <p class="bottomleft">포토샵/ 파일변환</p>
                    </v-card>
                    <v-card
                    class="category"
                    ><img src="@/assets/category-113@2x.png" alt="블로그, 카페">
                    <p class="bottomleft">상세/이벤트 페이지</p>
                    </v-card>
                    <v-card
                    class="category"
                    ><img src="@/assets/category-112@2x.png" alt="블로그, 카페">
                    <p class="bottomleft">블로그/SNS/썸네일</p>
                    </v-card>
                    </v-row>   
                </div>                       
            </div>
            <div style="padding: 20px; margin-left: auto; margin-right: auto; width: 1250px; height: 197.8px;">
                <img src="@/assets/out.png" alt="아웃소싱 배너" style="width: 1190px; height: 197.8px;">
            </div>
            <div style="padding: 35px; margin-left: auto; margin-right: auto; width: 1230px;">
            
            <h3>TOP 카테고리 전문가 랭킹</h3>
            <p style="color: #757575; font-size: 13px;">크몽에서 가장 많이 판매한 인기 전문가 랭킹입니다.</p>
            <v-row>
                <div class="TopSeller">    
                    <v-card
                    :loading="loading"
                    style="width: 378px; background-color: #eeeeee;">
                        <h3 class="text_c" style="margin-right: auto; margin-left: auto;">SNS 마케팅</h3>
                        <v-img
                        style="width: 318px; height: 126px; margin-right: auto; margin-left: auto;"
                        src="@/assets/first.png"
                        ></v-img>  
                        <div class="TopSellerItem">
                                <p class="col-xs-6 font-size-h4 NGB padding-side-0">2위 848,030,280원 모비딕 마케팅</p> 
                        </div>
                        <div class="TopSellerItem">
                                <p class="col-xs-6 font-size-h4 NGB padding-side-0">3위 780,329,300원 GPAKOREA</p> 
                        </div> 
                        <div class="TopSellerItem">
                                <p class="col-xs-6 font-size-h4 NGB padding-side-0">4위 675,636,600원 조아요</p> 
                        </div>
                        <div class="TopSellerItem">
                                <p class="col-xs-6 font-size-h4 NGB padding-side-0">5위 635,790,100원 소셜헬프코리아</p> 
                        </div>
                    </v-card>       
                </div>
                
                    </v-row>
                    
        </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Main',
    components: {

    }
}
</script>

<style>
    .bottomleft {
    position: absolute;
    bottom: 8px;
    left: 16px;
    font-size: 14px;
    color: white;
    font-weight: bold;
    }
    .plain_2{
        color: #757575;
    }
    .text_c{
        text-align: center;
        padding: 15px;
    }
    .TopSeller{
        padding-left: 30px;
        padding-top: 22px;
        padding-right: 30px;
        
    }
    .TopSellerItem{
        padding-top: 20px;
        padding-bottom: 20px;
        border-bottom: 1px solid #e6e6e6;
    }
    .category{
        position: relative; width: 237px; height: 150px;
    }
    .category img{
        widows: 220px;height:150px;
    }
</style>