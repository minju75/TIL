<template>
    <v-container>
        <v-row class="wrapBox">
            <div class="col-6">
                <p class="introduceMessage" style="padding-top:20px;">방문을 진심으로<br />환영합니다.</p>
                <div class="productBox">
                    <div class="newProducts">
                        <p>New 상품!</p>
                        <v-row class="newRow">
                            <v-item v-for="n in 3"
                            :key="n"
                            style="margin:0 16px;"
                            >
                                <div class="itemBox">
                               
                                </div>
                            </v-item>
                        </v-row>
                    </div>
                    <div class="saleProducts">
                        <p>Sale 상품!</p>
                        <v-row class="saleRow">
                            <v-item v-for="n in 3"
                            :key="n"
                            style="margin:0 16px;"
                            >
                                <div class="itemBox"></div>
                            </v-item>
                        </v-row>
                    </div>
                </div>
            </div>
            <div class="col-6 cambox">
                <vue-web-cam
                    ref="webcam"
                    :device-id="deviceId"
                    style="margin-top: 70px; "
                    width="100%"
                    height="580px"
                    @stopped="onStopped"
                    @error="onError"
                    @cameras="onCameras"
                    @camera-change="onCameraChange"
                />
                <div class="divider"></div>
                <p class="guideMessage mb-10">
                    얼굴을 가이드라인에 맞춰주시고 <br />인식이 완료될때까지 잠시 기다려주세요
                </p>
                
            </div>
        </v-row>
        <v-btn @click="goCamPayment">결제화면보기</v-btn>
    </v-container>
</template>

<script>
import { WebCam } from 'vue-web-cam';
export default {
    name: 'App',
    components: {
        'vue-web-cam': WebCam,
    },
    data() {
        return {
            img: null,
            camera: null,
            deviceId: null,
            devices: [],
        };
    },
    computed: {
        device: function() {
            return this.devices.find((n) => n.deviceId === this.deviceId);
        },
    },
    watch: {
        camera: function(id) {
            this.deviceId = id;
        },
        devices: function() {
            // Once we have a list select the first one
            const [first, ...tail] = this.devices; // eslint-disable-line no-unused-vars
            if (first) {
                this.camera = first.deviceId;
                this.deviceId = first.deviceId;
            }
        },
    },
    methods: {
        onCapture() {
            this.img = this.$refs.webcam.capture();
        },
        onStarted(stream) {
            console.log('On Started Event', stream);
        },
        onStopped(stream) {
            console.log('On Stopped Event', stream);
        },
        onStop() {
            this.$refs.webcam.stop();
        },
        onStart() {
            this.$refs.webcam.start();
        },
        onError(error) {
            console.log('On Error Event', error);
        },
        onCameras(cameras) {
            this.devices = cameras;
            console.log('On Cameras Event', cameras);
        },
        onCameraChange(deviceId) {
            this.deviceId = deviceId;
            this.camera = deviceId;
            console.log('On Camera Change Event', deviceId);
        },
        goCamPayment(){
            this.$router.push({name:'CamPayment'});
        }
    },
};
</script>
<style scoped>
@import '../assets/css/cam.css';

</style>
