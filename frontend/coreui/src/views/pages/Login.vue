<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <b-row class="justify-content-center">
        <b-col md="8">
          <b-alert show variant="danger" v-if="errors.length > 0">
              <h4 class="alert-heading">Error !</h4>
              <ul>
                <li v-for="item in errors" :key="item">{{ item }}</li>
              </ul>
              <hr>
              <p class="mb-0">
               Silahkan periksa kembali isian anda.
              </p>
            </b-alert>
          <b-card-group>
            <b-card no-body class="p-4">
              <b-card-body>
                <b-form>
                  <h1>Login</h1>
                  <p class="text-muted">Masuk dengan akun anda</p>
                  <b-input-group class="mb-3">
                    <b-input-group-prepend><b-input-group-text><i class="icon-user"></i></b-input-group-text></b-input-group-prepend>
                    <b-form-input type="text" class="form-control" placeholder="Username" autocomplete="username email" v-model="username" />
                  </b-input-group>
                  <b-input-group class="mb-4">
                    <b-input-group-prepend><b-input-group-text><i class="icon-lock"></i></b-input-group-text></b-input-group-prepend>
                    <b-form-input type="password" class="form-control" placeholder="Password" autocomplete="current-password" v-model="password"/>
                  </b-input-group>
                  <b-row>
                    <b-col cols="6">
                      <b-button variant="warning" class="px-4" @click="checkForm">Login</b-button>
                    </b-col>
                    <b-col cols="6" class="text-right">
                      <b-button variant="link" class="px-0">Lupa password?</b-button>
                    </b-col>
                  </b-row>
                </b-form>
              </b-card-body>
            </b-card>
            <b-card no-body class="text-white bg-warning py-5 d-md-down-none" style="width:44%">
              <b-card-body class="text-center">
                <div>
                  <h2>Sign up</h2>
                  <p>Anda merasa belum memiliki akun ?, anda harus mendaftarkan akun anda terlebih dahulu </p>
                  <b-button variant="primary" class="active mt-3" @click="toRegis">Daftar Sekarang!</b-button>
                </div>
              </b-card-body>
            </b-card>
          </b-card-group>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
import PostsService from '@/services/PostsService'
export default {
  name: 'Login',
  data: function(){
    return{
       errors: []
    }
   
  },
  methods:{
    toRegis(){
      this.$router.push({ name: 'Register' })
    },
    checkForm:function(e){
      if(this.username && this.password ){
        this.postData();
      }
      this.errors = []
      if(!this.username){
        this.errors.push('Username tidak boleh kosong');
      }
      if(!this.password){
        this.errors.push('Password tidak boleh kosong');
      }
      e.preventDefault();
    },
    async postData() {
      const response = await PostsService.loginPost({
                          username: this.username,
                          password: this.password
                        });
      if(response.data.success){
          console.log(response.data)
      }
      
    }
  }
}
</script>
