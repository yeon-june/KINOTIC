<template>
  <div class="flex flex-col justify-center items-center" :class="{ 'overflow-hidden' : showModal}" id="wrap">
    <SignupModal v-if="showModal" @close="showModal = false" id="modal">
      <!-- 1-1) 모달 헤더 -->
      <h3 slot="header" class="bc-card modal-text flex items-center text-xl pl-1">이용 약관 동의</h3> 
      <!-- 1-2) 모달 푸터 -->
      <span slot="body">
        <form action="">
          <div class="ml-1 mb-2 flex items-center">
            <input type="checkbox" class="mr-2" required v-model="usageAgree">
            <span class="text-lg"> KINOTIC 이용약관 동의 (필수)</span>
          </div>
          <div class="p-container px-3 py-4">
            <strong>여러분을 환영합니다.</strong>
            <br> <br>
            KINOTIC 서비스 및 제품(이하 ‘서비스’)을 이용해 주셔서 감사합니다. 본 약관은 다양한 KINOTIC 서비스의 이용과 관련하여 KINOTIC 서비스를 제공하는 난쟁's와 이를 이용하는 KINOTIC 서비스 회원(이하 ‘회원’) 또는 비회원과의 관계를 설명하며, 아울러 여러분의 KINOTIC 서비스 이용에 도움이 될 수 있는 유익한 정보를 포함하고 있습니다.
            <br> <br>
            KINOTIC 서비스를 이용하시거나 KINOTIC 서비스 회원으로 가입하실 경우 여러분은 본 약관 및 관련 운영 정책을 확인하거나 동의하게 되므로, 잠시 시간을 내시어 주의 깊게 살펴봐 주시기 바랍니다.
            <br> <br>
            <strong>다양한 KINOTIC 서비스를 즐겨보세요.</strong>
            <br> <br>
            KINOTIC은 웹사이트를 통해 영화 정보 검색, 사용자 기반 영화 추천 서비스, 다른 이용자와의 커뮤니케이션 등 여러분의 영화 시청 생활에 활기를 더할 수 있는 다양한 서비스를 제공하고 있습니다.
            <br> <br>
            <strong>회원으로 가입하시면 KINOTIC 서비스를 보다 편리하게 이용할 수 있습니다</strong>
            <br> <br>
            여러분은 본 약관을 읽고 동의하신 후 회원 가입을 신청하실 수 있으며, KINOTIC은 이에 대한 승낙을 통해 회원 가입 절차를 완료하고 여러분께 KINOTIC 서비스 이용 계정(이하 ‘계정’)을 부여합니다. 계정이란 회원이 KINOTIC 서비스에 로그인한 이후 이용하는 각종 서비스 이용 이력을 회원 별로 관리하기 위해 설정한 회원 식별 단위를 말합니다. 회원은 자신의 계정을 통해 좀더 다양한 KINOTIC 서비스를 보다 편리하게 이용할 수 있습니다.
            <br> <br>
            <strong>여러분이 제공한 콘텐츠를 소중히 다룰 것입니다.</strong>
            <br> <br>
            KINOTIC은 여러분이 게재한 게시물이 KINOTIC 서비스를 통해 다른 이용자들에게 전달되어 풍족해질 여가 생활을 기대합니다. 게시물은 여러분이 타인 또는 자신이 보게 할 목적으로 KINOTIC 서비스 상에 게재한 부호, 문자, 음성, 음향, 그림, 사진, 동영상, 링크 등으로 구성된 각종 콘텐츠 자체 또는 파일을 말합니다.
            <br> <br>
            KINOTIC는 여러분의 생각과 감정이 표현된 콘텐츠를 소중히 보호할 것을 약속 드립니다. 여러분이 제작하여 게재한 게시물에 대한 지식재산권 등의 권리는 여러분에게 있습니다.
            <br> <br>
            한편, KINOTIC 서비스를 통해 여러분이 게재한 게시물을 적법하게 제공하려면 해당 콘텐츠에 대한 저장, 복제, 수정, 공중 송신, 전시, 배포, 2차적 저작물 작성(단, 번역에 한함) 등의 이용 권한(기한과 지역 제한에 정함이 없으며, 별도 대가 지급이 없는 라이선스)이 필요합니다. 게시물 게재로 여러분은 KINOTIC에게 그러한 권한을 부여하게 되므로, 여러분은 이에 필요한 권리를 보유하고 있어야 합니다.
            <br> <br>
            KINOTIC은 여러분이 부여해 주신 콘텐츠 이용 권한을 저작권법 등 관련 법령에서 정하는 바에 따라 KINOTIC 서비스 내 노출, 서비스 홍보를 위한 활용, 서비스 운영, 개선 및 새로운 서비스 개발을 위한 연구, 웹 접근성 등 법률상 의무 준수, 외부 사이트에서의 검색, 수집 및 링크 허용을 위해서만 제한적으로 행사할 것입니다. 만약, 그 밖의 목적을 위해 부득이 여러분의 콘텐츠를 이용하고자 할 경우엔 사전에 여러분께 설명을 드리고 동의를 받도록 하겠습니다.
            <br> <br>
            또한 여러분이 제공한 선호 데이터(좋아요, 봤어요 등)는 KINOTIC 서비스를 개선하고 새로운 KINOTIC 서비스를 제공하기 위해 사용자 기반 영화 추천 서비스 개발 목적으로 KINOTIC에서 사용될 수 있습니다. KINOTIC는 지속적인 연구 개발을 통해 여러분께 좀 더 편리하고 유용한 서비스를 제공해 드릴 수 있도록 최선을 다하겠습니다.
            <br> <br>
            KINOTIC은 여러분이 자신이 제공한 콘텐츠에 대한 KINOTIC 또는 다른 이용자들의 이용 또는 접근을 보다 쉽게 관리할 수 있도록 다양한 수단을 제공하기 위해 노력하고 있습니다. 여러분은 KINOTIC 서비스 내에 콘텐츠 삭제, 비공개 등의 관리기능이 제공되는 경우 이를 통해 직접 타인의 이용 또는 접근을 통제할 수 있고, 고객센터를 통해서도 콘텐츠의 삭제, 비공개, 검색결과 제외 등의 조치를 요청할 수 있습니다. 다만, 일부 KINOTIC 서비스의 경우 삭제, 비공개 등의 처리가 어려울 수 있으며, 이러한 내용은 각 서비스 상의 안내, 공지사항, 고객센터 도움말 등에서 확인해 주시길 부탁 드립니다.
            <br> <br>
            <strong>KINOTIC 서비스 이용과 관련하여 몇 가지 주의사항이 있습니다.</strong>
            <br> <br>
            KINOTIC은 여러분이 KINOTIC 서비스를 자유롭고 편리하게 이용할 수 있도록 최선을 다하고 있습니다. 다만, 여러분이 KINOTIC 서비스를 보다 안전하게 이용하고 KINOTIC 서비스에서 여러분과 타인의 권리가 서로 존중되고 보호받으려면 여러분의 도움과 협조가 필요합니다. 여러분의 안전한 서비스 이용과 권리 보호를 위해 부득이 아래와 같은 경우 여러분의 게시물 게재나 KINOTIC 서비스 이용이 제한될 수 있으므로, 이에 대한 확인 및 준수를 요청 드립니다.
            <br> <br>
            - 회원 가입 시 이름, 생년월일, 휴대전화번호 등의 정보를 허위로 기재해서는 안 됩니다. 회원 계정에 등록된 정보는 항상 정확한 최신 정보가 유지될 수 있도록 관리해 주세요. 자신의 계정을 다른 사람에게 판매, 양도, 대여 또는 담보로 제공하거나 다른 사람에게 그 사용을 허락해서는 안 됩니다. 아울러 자신의 계정이 아닌 타인의 계정을 무단으로 사용해서는 안 됩니다. 이에 관한 상세한 내용은 계정 운영정책을 참고해 주시기 바랍니다.
            <br>
            - 타인에 대해 직접적이고 명백한 신체적 위협을 가하는 내용의 게시물, 타인의 자해 행위 또는 자살을 부추기거나 권장하는 내용의 게시물, 타인의 신상정보, 사생활 등 비공개 개인정보를 드러내는 내용의 게시물, 타인을 지속적으로 따돌리거나 괴롭히는 내용의 게시물, 성매매를 제안, 알선, 유인 또는 강요하는 내용의 게시물, 공공 안전에 대해 직접적이고 심각한 위협을 가하는 내용의 게시물은 제한될 수 있습니다.
            <br>
            - 관련 법령상 금지되거나 형사처벌의 대상이 되는 행위를 수행하거나 이를 교사 또는 방조하는 등의 범죄 관련 직접적인 위험이 확인된 게시물, 관련 법령에서 홍보, 광고, 판매 등을 금지하고 있는 물건 또는 서비스를 홍보, 광고, 판매하는 내용의 게시물, 타인의 지식재산권 등을 침해하거나 모욕, 사생활 침해 또는 명예훼손 등 타인의 권리를 침해하는 내용이 확인된 게시물은 제한될 수 있습니다.
            <br>
            - 자극적이고 노골적인 성행위를 묘사하는 등 타인에게 성적 수치심을 유발시키거나 왜곡된 성 의식 등을 야기할 수 있는 내용의 게시물, 타인에게 잔혹감 또는 혐오감을 일으킬 수 있는 폭력적이고 자극적인 내용의 게시물, 본인 이외의 자를 사칭하거나 허위사실을 주장하는 등 타인을 기만하는 내용의 게시물, 과도한 욕설, 비속어 등을 계속하여 반복적으로 사용하여 심한 혐오감 또는 불쾌감을 일으키는 내용의 게시물은 제한될 수 있습니다.
            <br>
            - 자동화된 수단을 활용하는 등 KINOTIC 서비스의 기능을 비정상적으로 이용하여 게재된 게시물, KINOTIC 각 개별 서비스의 제공 취지와 부합하지 않는 내용의 게시물은 다른 이용자들의 정상적인 KINOTIC 서비스 이용에 불편을 초래하고 더 나아가 KINOTIC의 원활한 서비스 제공을 방해하므로 역시 제한될 수 있습니다. 기타 제한되는 게시물에 관한 상세한 내용은 게시물 운영정책 및 각 개별 서비스에서의 약관, 운영정책 등을 참고해 주시기 바랍니다.
            <br>
            - KINOTIC의 사전 허락 없이 자동화된 수단(예: 매크로 프로그램, 로봇(봇), 스파이더, 스크래퍼 등)을 이용하여 KINOTIC 서비스 회원으로 가입을 시도 또는 가입하거나, KINOTIC 서비스에 로그인을 시도 또는 로그인하거나, KINOTIC 서비스 상에 게시물을 게재하거나, KINOTIC 서비스를 통해 커뮤니케이션하거나(예: 전자메일, 쪽지 등), KINOTIC 서비스에 게재된 회원의 아이디(ID), 게시물 등을 수집하거나, KINOTIC 검색 서비스에서 특정 질의어로 검색하거나 혹은 그 검색결과에서 특정 검색결과를 선택(이른바 ‘클릭’)하는 등 이용자(사람)의 실제 이용을 전제로 하는 KINOTIC 서비스의 제공 취지에 부합하지 않는 방식으로 KINOTIC 서비스를 이용하거나 이와 같은 KINOTIC 서비스에 대한 어뷰징(남용) 행위를 막기 위한 KINOTIC의 기술적 조치를 무력화하려는 일체의 행위(예: IP를 지속적으로 바꿔가며 접속하는 행위, Captcha를 외부 솔루션 등을 통해 우회하거나 무력화 하는 행위 등)를 시도해서는 안 됩니다.
            <br>
            - KINOTIC의 동의 없이 자동화된 수단에 의해 KINOTIC 서비스 상에 광고가 게재되는 영역 또는 그 밖의 영역에 부호, 문자, 음성, 음향, 그림, 사진, 동영상, 링크 등으로 구성된 각종 콘텐츠 자체 또는 파일을 삽입해서는 안 됩니다. 또한, KINOTIC 서비스 또는 이에 포함된 소프트웨어를 복사, 수정할 수 없으며, 이를 판매, 양도, 대여 또는 담보로 제공하거나 타인에게 그 이용을 허락해서는 안 됩니다. KINOTIC 서비스에 포함된 소프트웨어를 역 설계, 소스코드 추출 시도, 복제, 분해, 모방, 기타 변형하는 등의 행위도 금지됩니다(다만, 오픈소스에 해당되는 경우 그 자체 조건에 따릅니다). 그 밖에 바이러스나 기타 악성 코드를 업로드하거나 KINOTIC 서비스의 원활한 운영을 방해할 목적으로 서비스 기능을 비정상적으로 이용하는 행위 역시 금지됩니다.
            <br>
            <br>
            본 약관은 한국어를 정본으로 합니다. 본 약관 또는 KINOTIC 서비스와 관련된 여러분과 KINOTIC와의 관계에는 대한민국의 법령이 적용됩니다. 그리고 본 약관 또는 KINOTIC 서비스와 관련하여 여러분과 KINOTIC 사이에 분쟁이 발생할 경우, 그 분쟁의 처리는 대한민국 '민사소송법'에서 정한 절차를 따릅니다.
            <br><br>
            <hr><br>
            공지 일자: 2022년 05월 25일 <br> 
            적용 일자: 2022년 05월 27일
          </div>

          <div class="ml-1 mb-2 flex items-center mt-6">
            <input type="checkbox" class="mr-2" required v-model="dataAgree">
            <span class="text-lg">개인정보 수집 및 이용 동의 (필수)</span>
          </div>
          <p class="p-container1 p-3">개인정보보호법에 따라 KINOTIC에 회원가입 신청하시는 분께 수집하는 개인정보의 항목, 개인정보의 수집 및 이용목적, 개인정보의 보유 및 이용기간, 동의 거부권 및 동의 거부 시 불이익에 관한 사항을 안내 드리오니 자세히 읽은 후 동의하여 주시기 바랍니다.</p>
        </form>
          <div class="flex justify-center mt-7">
            <button class="text-lg" @click.prevent="onAgree">확인</button>
          </div>
      </span>
    </SignupModal>
    <div class="center flex flex-col justify-center items-center mt-2">

      <img src="@/assets/signup.png" alt="signup img" id="signup-img" class="mb-8">

      <account-error-list v-if="authError"></account-error-list>

      <form @submit.prevent="signup(credentials)" id="signup-form" class="flex flex-col justify-center items-center">
        <div id="input-div" class="flex flex-col">
          <label for="username" class="mb-1">Username</label>
          <input  v-model="credentials.username" type="text" id="username" class="px-2" autocomplete="off" required/>
        </div>
        <div id="input-div" class="flex flex-col mt-5">
          <label for="password1" class="mb-1">Password</label>
          <input v-model="credentials.password1" type="password" id="password1" class="px-2" autocomplete="off" required />
        </div>
        <div id="input-div" class="flex flex-col mb-5">
          <label for="password2" class="mb-1">Password Confirmation</label>
          <input v-model="credentials.password2" type="password" id="password2" class="px-2" autocomplete="off" required />
        </div>
        <div id="input-div" class="flex flex-col mb-6">
          <label for="email" class="mb-1">Email</label>
          <input v-model="credentials.email" type="text" id="email" class="px-2" autocomplete="off" required />
        </div>
        <div class="flex items-center mb-3">
        <input type="checkbox" v-model="agreement" class="mr-2" @click.prevent="openModal" required>
        <p>회원가입을 위해 약관에 동의해 주세요</p>
        </div>
        <button>Submit</button>
      </form>
      <div class="flex items-center mt-2">
        <a href="/">HOME</a>
        <p class="mx-3 text-sm">|</p>
        <a href="/login">LOGIN</a>
      </div>

    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'
  import SignupModal from '@/components/SignupModal.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
      SignupModal,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
          email: '',
        },
        showModal: false,
        usageAgree: false,
        dataAgree: false,
      }
    },
    computed: {
      ...mapGetters(['authError', 'isLoggedIn']),
      agreement() {
        return this.usageAgree && this.dataAgree
      }
    },
    methods: {
      ...mapActions(['signup']),
      onAgree(){
          this.showModal = false
          this.agreement = true
      },
      openModal(){
        this.showModal = true
      }
    },
    created(){
      console.log(document.referrer)
      if (this.isLoggedIn) {
        document.location.href = "/"
      }
    }
  }
</script>

<style scoped>
#wrap {
  display: grid;
  place-items: center;
  min-height: 90vh;
}

#full-screen{
  height:100vh;
  overflow:hidden;
}

#signup-img{
  width:30%;
}

#signup-form{
  width:85%;
  height:480px;
  min-height: 400px;
  max-height: 500px;
  background-color: #FFF2BF;
  border-radius: 20px;
}

#input-div{
  width:80%;
}

.w-85{
  width:85%;
}
.p-container{
  border: solid 0.1px #d8d8d8;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 0px 0px 1px;
  overflow-y:scroll !important; 
  height:250px !important;
  text-align: justify;
}

.p-container1{
  border: solid 0.1px #d8d8d8;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 0px 0px 1px;
  text-align: justify;
}

.p-container::-webkit-scrollbar {
    width: 8px;  /* 스크롤바의 너비 */
}

.p-container::-webkit-scrollbar-thumb {
    height: 20%; /* 스크롤바의 길이 */
    background: #9486CD; /* 스크롤바의 색상 */
    
    border-radius: 10px;
}

.p-container::-webkit-scrollbar-track {
    background: rgba(141, 40, 235, 0.1);  /*스크롤바 뒷 배경 색상*/
}

input[type="text"]{
  width: 100%;
  height: 5vh;
  min-height: 30px;
  max-height: 45px;
  border-radius: 10px;
  background-color:white;
}

input[type="password"]{
  width: 100%;
  height: 5vh;
  min-height: 35px;
  max-height: 45px;
  border-radius: 10px;
  background-color:white;
}

button{
  height:45px;
  background-color: #BCA7D2;
  width:25%;
  border-radius:10px;
  color:white;
}

input[type="checkbox"] {
    -webkit-appearance: none;
    position: relative;
    width: 20px !important;
    height: 20px !important;
    cursor: pointer;
    outline: none !important;
    border: 1px solid #e0e0e0;
    border-radius: 2px;
    background: #fbfbfb;
    box-shadow: rgba(0, 0, 0, 0.05) 0px 0px 0px 1px;

}

input[type="checkbox"]::before {
    content: "✔";
    position: absolute;
    top: 50%;
    left: 50%;
    overflow: hidden;
    transform: scale(0) translate(-50%, -50%);
    line-height: 1;
}

input[type="checkbox"]:hover {
    border-color: rgba(170, 170, 170, 0.5);
}

input[type="checkbox"]:checked {
    background-color: #8769b8;
    border-color: rgba(255, 255, 255, 0.3);
    color: white;
}

input[type="checkbox"]:checked::before {
    border-radius: 2px;
    transform: scale(1) translate(-50%, -50%)
}
</style>
