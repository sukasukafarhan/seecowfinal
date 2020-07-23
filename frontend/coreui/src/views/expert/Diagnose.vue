<template>
  <div class="wrapper">
    <div class="animated fadeIn">
      <b-row>
        <b-col lg="12" md="12">
          <!-- show-progress -->
          <!-- <b-progress :value="progress_counter" variant="warning" :max="progress_max" animated></b-progress> -->
           
         </b-col>
      </b-row>
      <br>
      <b-row>
         <b-col lg="2" md="2">
         </b-col>
         <b-col lg="8" md="8">
           <b-card class="card-accent-warning"
        header-tag="header"
        footer-tag="footer">
        <div slot="header">
           <img src="img/cow/cow (2).png" width="50px" alt="CoreUI Logo"><strong> Cow</strong>
          <!-- <div class="card-header-actions">
            <a href="https://bootstrap-vue.js.org/docs/components/progress" class="card-header-action" rel="noreferrer noopener" target="_blank">
              <small class="text-muted">docs</small>
            </a>
          </div> -->
        </div>
        <div>
          <h6 class="text-muted" style="text-align:center">Please fill the symptom survey below to find out what is happening to your cow</h6>
          <!-- <ul id="example-1">
            <li v-for="item in dataAttribute" :key="item._id">
              {{ item.namaAttribute }}
            </li>
          </ul> -->
          <b-tabs pills v-model="tabIndex">
            <b-tab title="First">  
              <b-row v-for="(item, index) in dataAttribute" :key="item.attributeIdentitiy" v-if="item.attributeIdentitiy<20" >
                <b-col sm="12" md="8" lg="8">
                  <h3> {{item.attributeIdentitiy+1}}. {{ item.namaAttribute }}</h3>
                </b-col>
                <b-col sm="12" md="4" lg="4">
                  <b-form-group v-on:submit="doDiagnose">
                    <b-form-select v-model="userResponses[index]"
                      :plain="true"
                      :options="[
                        {
                          text: 'Tidak ',
                          value: '0'
                        }, {
                          text: 'Mungkin',
                          value: '0.3'
                        }, {
                          text: 'Kemungkinan Besar',
                          value: '0.5'
                        }, {
                          text: 'Hampir Pasti',
                          value: '0.7'
                        }, {
                          text: 'Pasti',
                          value: '1'
                        }]">
                    </b-form-select>
                  </b-form-group>
                </b-col> 
                <hr>          
              </b-row>
            </b-tab>

            <b-tab title="Second">  
              <b-row v-for="(item, index) in dataAttribute" :key="item.attributeIdentitiy" v-if="item.attributeIdentitiy>=20" >
                <b-col sm="12" md="8" lg="8">
                  <h3> {{item.attributeIdentitiy+1}}. {{ item.namaAttribute }}</h3>
                </b-col>
                <b-col sm="12" md="4" lg="4">
                  <b-form-group v-on:submit="doDiagnose">
                    <b-form-select v-model="userResponses[index]"
                      :plain="true"
                      :options="[
                        {
                          text: 'Tidak',
                          value: '0'
                        }, {
                          text: 'Mungkin',
                          value: '0.3'
                        }, {
                          text: 'Kemungkinan Besar',
                          value: '0.5'
                        }, {
                          text: 'Hampir Pasti',
                          value: '0.7'
                        }, {
                          text: 'Pasti',
                          value: '1'
                        }]">
                    </b-form-select>
                  </b-form-group>
                </b-col>           
              </b-row>
                <table style="float:right">
                  <tr>
                    <td>
                        <b-btn class="mt-4" id="asd2"  variant="danger" @click="doDiagnose">Diagnose</b-btn>
                    </td>
                    </tr>
                </table>
            </b-tab>
          </b-tabs>
          <hr>
        </div>
      </b-card>
      <b-card header="System Advice" class="card-accent-danger">
         <b-progress v-if="ansArray.length == 0" :value="progress_counter" variant="warning" :max="progress_max" animated></b-progress>
        <!-- <h5 class="text-muted" style="text-align:center" v-if="ansArray.length > 0">System Advice</h5> -->
          <div role="tablist" v-if="ansArray.length > 0">
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-btn block href="#" v-b-toggle.accordion1 variant="danger">{{ansArray[0]}} / {{ansArray[3].toFixed(2)*100}} %</b-btn>
              </b-card-header>
              <b-collapse id="accordion1" visible accordion="my-accordion" role="tabpanel">
                <b-card-body>
                  <b-card no-body>
                    <b-tabs>
                      <b-tab active>
                          <template slot="title">
                            <strong>Symptoms summary</strong>
                          </template>
                           <b-table striped outlined stacked="sm" hover :items="tableItems" :fields="tableFields" head-variant="light">
                          <template v-slot:cell(key-question)="data">
                            {{data.item.namaAttributes}}
                           <!-- {{data.item.nilai == 0 ? "No":"Yes"  }} -->
                          </template>
                          <template v-slot:cell(key-answer)="data">
                            <b-badge :variant="getStatus(data.item.nilai)">
                              <p v-if="data.item.nilai == 0.3">Mungkin</p>
                              <p v-else-if="data.item.nilai == 0.5">Kemungkinan Besar</p>
                              <p v-else-if="data.item.nilai == 0.7">Hampir Pasti</p>
                              <p v-else-if="data.item.nilai == 1">Pasti</p>
                            </b-badge>
                          </template>
                          </b-table>
                      </b-tab>
                      <b-tab active>
                          <template slot="title">
                            <strong>Prevention advice</strong>
                          </template>
                          <strong>{{ansArray[2]}}</strong>
                      </b-tab>
                       <b-tab>
                          <template slot="title">
                            <strong>Treatment advice</strong>
                          </template>
                          <strong>{{ansArray[1]}}</strong>
                      </b-tab>
                    </b-tabs>
                  </b-card>
                </b-card-body>
              </b-collapse>
            </b-card>
            
          </div>
      </b-card>
         </b-col>
         <b-col lg="2" md="2">
         </b-col>
      </b-row>
 
    </div>
  </div>
</template>

<script>
import Constants from "@/services/Constants"
import PostsService from "@/services/PostsService"
export default {
  name: 'expert',
  data () {
    return {
      tabIndex: 0,
      progress_counter: 0,
      progress_max: 0,
      dataAttribute:[],
      userResponses: [],
      ansArray:[],
      tableItems: [],
      tableFields: [
        {
          key:'key-question',
          label: 'Symptoms'
          
        },
        {
          key:'key-answer',
          label:'Condition'
        }
      ],
      bars: [
        {variant: 'success', value: 75},
        {variant: 'info', value: 75},
        {variant: 'warning', value: 75},
        {variant: 'danger', value: 75},
        {variant: 'primary', value: 75},
        {variant: 'secondary', value: 75},
        {variant: 'dark', value: 75}
      ],
      timer: null,
      striped: true,
      animate: true,
      max3: 100,
      values: [ 15, 30, 20 ]
    }
  },
  created(){
    this.checkSession(); 
  },
  methods: {
    checkSession(){
      /**
       * check session and do action
       */
      if(!window.localStorage.getItem("token")){
        this.$router.push({ name: 'Login' })  
      }else{
        if(window.localStorage.getItem("role") != Constants.ROLE_FARMERS){
          // redirect to 404 page
           this.$router.push({ name: 'Page404' })  
        }else{
            this.firstLoad();
        }
        
      }
    },
    async fetchDataAttribute(){
      const response = await PostsService.getAllAttributes();
      return response.data;
    },
    async firstLoad(){
      // console.log(window.localStorage.getItem("token"));
      const response = await this.fetchDataAttribute();
      let attributeData = response.data;
      this.dataAttribute = attributeData
      this.progress_max = this.dataAttribute.length
      this.userResponses = Array(this.dataAttribute.length).fill(0)
      // console.log(this.dataAttribute[0].namaAttribute)
      
    },
    async ToServer(params,id_sapi){
      const response = await PostsService.testingData(params,id_sapi);
      return response.data;
    },
    getStatus(tmp){
      return tmp == 0 ? 'danger' : 'success'
    },
    clicked () {
      // console.log(this.tabIndex)
      if(this.progress_counter == this.progress_max){
        // console.log("max===")
        this.progress_counter = this.progress_max
      }else{
        this.tabIndex++;
        this.progress_counter++; 
      }
    },
    prev () {
      this.ansArray=[]
      if(this.progress_counter == 0){
        this.tabIndex = 0;
        this.progress_counter = 0;
      }else{
        this.tabIndex--;
        this.progress_counter--;
      }
      
    },
    async doDiagnose(){
      this.ansArray=[]
      if(this.progress_counter == this.progress_max){
        // console.log("max===")
        this.progress_counter = this.progress_max
      }else{
        this.progress_counter++
      }
      
      var objData = [] // empty array
      // objData[0][this.dataAttribute[0].namaAttribute] = this.userResponses[0]
      for (var i = 0; i < this.userResponses.length; i++) {
        if (this.userResponses[i] != '0') {
          objData.push({
            gejala: this.dataAttribute[i].namaAttribute,
            cfuser: this.userResponses[i]
          })
        } 
        // else {
        //   objData.push({
        //     gejala: this.dataAttribute[i].namaAttribute,
        //     cfuser: 0
        //   })
        // }
      }
      console.log(objData)
      // var objData = [{}] // empty array
      // for(var i=0;i<this.dataAttribute.length;i++){
      //   objData[0][this.dataAttribute[i].namaAttribute] = this.userResponses[i]
      // }
      const response = await this.ToServer(objData,this.$route.params.id)
      let dataFinal = response.data
      this.ansArray.push(dataFinal.diagnose)
      this.ansArray.push(dataFinal.treatment)
      this.ansArray.push(dataFinal.prevention)
      this.ansArray.push(dataFinal.nilai)
      this.tableItems = dataFinal.gejala
      // console.log(objData[0])
    }
  }
}
</script>

