<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <b-row class="justify-content-center">
        <!-- <h4>{{anu}}</h4> -->
        <b-col md="8">
          <b-alert show variant="danger" v-if="errors.length > 0">
              <h4 class="alert-heading">Error !</h4>
              <ul>
                <li v-for="item in errors" :key="item">{{ item }}</li>
              </ul>
              <hr>
              <p class="mb-0">
               Please check again your form field.
              </p>
          </b-alert>
          <b-card-group>
            <b-card no-body class="p-4">
              <b-card-body>
                <b-form>
                  <h1>Login</h1>
                  <p class="text-muted">Login with yout account</p>
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
                      <b-button variant="link" class="px-0">Forgot password?</b-button>
                    </b-col>
                  </b-row>
                </b-form>
              </b-card-body>
            </b-card>
            <b-card no-body class="text-white bg-warning py-5">
              <b-card-body class="text-center">
                <div>
                  <h2>Sign up</h2>
                  <p>You feel you don't have an account? You must register your account first</p>
                  <b-button variant="primary" class="active mt-3" @click="toRegis">Register now!</b-button>
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
import io from 'socket.io-client';
export default {
  name: 'Login',
  data: function(){
    return{
       username:"",
       password:"",
       anu:"",
      //  socket : io('localhost:3001'),
       errors: []
    }
   
  },
  // created(){
  //   //  var socket = io();
  //   //  socket.on('chat message', function(msg){
  //   //   this.anu=msg
  //   //  });
  //   this.nganu();
  // },
  methods:{
    // nganu(){
    // //  var socket = io('http://localhost');
    // //   socket.on('stream', function(data){
    // //     this.anu = data.title;
    // //   }); 
    //    this.socket.on('/topic/coba', (data) => {
    //         this.anu = data[0]._id;
    //         // you can also do this.messages.push(data)
    //     });
    // },
    toRegis(){
      this.$router.push({ name: 'Register' })
    },
    checkForm:function(e){
      if(this.username && this.password ){
        this.postData();
      }
      this.errors = []
      if(!this.username){
        this.errors.push('Username cant blank !');
      }
      if(!this.password){
        this.errors.push('Password cant blank !');
      }
      e.preventDefault();
    },
    async postData() {
      const response = await PostsService.loginPost({
                          username: this.username,
                          password: this.password
                        });
      if(response.data.success){
          // window.localStorage.setItem("token",response.data.token)
          // this.$router.push({ name: 'Dashboard' })
          // console.log(response.data)
          this.getMe(response.data.token)
      }else{
         this.errors = []
         this.errors.push('Wrong username or password !');
      }
      
    },
    async getMe(token){
      const response = await PostsService.me(token);
       window.localStorage.setItem("token",token)
       window.localStorage.setItem("peternak_id",response.data.peternak._id)
       this.$router.push({ name: 'Dashboard' })
      // console.log(items);
    }

  }
}
</script>
