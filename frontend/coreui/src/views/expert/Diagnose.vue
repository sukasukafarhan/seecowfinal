<template>
  <div class="wrapper">
    <div class="animated fadeIn">
      <b-row>
        <b-col lg="12" md="12">
          <!-- show-progress -->
          <b-progress :value="progress_counter" variant="warning" :max="progress_max" animated></b-progress>
           
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
          <h6 class="text-muted" style="text-align:center">Please fill yes or no in the symptom survey below to find out what is happening to your cow</h6>
          <!-- <ul id="example-1">
            <li v-for="item in dataAttribute" :key="item._id">
              {{ item.namaAttribute }}
            </li>
          </ul> -->
          <b-tabs pills v-model="tabIndex">
            <b-tab v-for="(item, index) in dataAttribute" :key="item.attributeIdentitiy" >
              <h3> {{ item.namaAttribute }}</h3>
              <br>
              <b-form-group :label-cols="1" :horizontal="true">
                <b-form-radio-group
                  stacked>
                  
                     <label>
                      
                      <input type="radio" 
                            v-bind:value="1" 
                            v-bind:name="index" 
                            v-model="userResponses[index]"> Yes
                    </label>
                    <br>
                    <label>
                      <input type="radio" 
                            v-bind:value="0" 
                            v-bind:name="index" 
                            v-model="userResponses[index]"> No
                    </label>
                  
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
           
          </b-tabs>
          <hr>
          <h5 class="text-muted" style="text-align:center" v-if="ansArray.length > 0">System Advice</h5>
          <div role="tablist" v-if="ansArray.length > 0">
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-btn block href="#" v-b-toggle.accordion1 variant="info">Mastitis : {{sameMastitisRules}}%</b-btn>
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
                          <div slot="key-question" slot-scope="data">
                            {{data.item.question}}
                           
                          </div>
                          <div slot="key-answer" slot-scope="data">
                            
                            <b-badge :variant="getStatus(data.item.answer)">{{questionStatus}}</b-badge>
                          </div>
                          </b-table>
                      </b-tab>
                      <b-tab>
                          <template slot="title">
                            <strong>Prevention advice</strong>
                          </template>
                          <ul>
                            <li>
                              Keep the cage clean
                            </li>
                            <li>
                              Clean the mammary glands regularly
                            </li>
                            <li>
                              Use antiseptics (iodine and chlorine fluids.) for dyeing nipples before and after milking
                            </li>
                          </ul>
                      </b-tab>
                       <b-tab>
                          <template slot="title">
                            <strong>Treatment advice</strong>
                          </template>
                          <ul>
                            <li>
                              Administration of cloxacillin antibiotics when dry cages
                            </li>
                            <li>
                              Give Suanovil (spiramycin) antibiotics directly to the nipple
                            </li>
                            
                          </ul>
                      </b-tab>
                    </b-tabs>
                  </b-card>
                </b-card-body>
              </b-collapse>
            </b-card>
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-btn block href="#" v-b-toggle.accordion2 variant="info">FootRoot : {{sameFootrootRules}}%</b-btn>
              </b-card-header>
              <b-collapse id="accordion2" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                  <b-card no-body>
                    <b-tabs>
                      <b-tab active>
                          <template slot="title">
                            <strong>Symptoms summary</strong>
                          </template>
                          <b-table striped outlined stacked="sm" hover :items="tableItems" :fields="tableFields" head-variant="light">
                          <div slot="key-question" slot-scope="data">
                            {{data.item.question}}
                           
                          </div>
                          <div slot="key-answer" slot-scope="data">
                            
                            <b-badge :variant="getStatus(data.item.answer)">{{questionStatus}}</b-badge>
                          </div>
                          </b-table>
                      </b-tab>
                      <b-tab>
                          <template slot="title">
                            <strong>Prevention advice</strong>
                          </template>
                          <ul>
                            <li>
                              Keep the cage floor clean and dry
                            </li>
                            <li>
                              Cages are disinfected once or twice a da
                            </li>
                            
                          </ul>
                      </b-tab>
                       <b-tab>
                          <template slot="title">
                            <strong>Treatment advice</strong>
                          </template>
                         <ul>
                            <li>
                              Place the sufferer in a dry cage
                            </li>
                            <li>
                              Clean infected feet, so they are free of dirt
                            </li>
                            <li>
                              The wound is then covered with sanitary napkins and cotton that have been given medicine, such as ichtyol ointment, sulfate solution, 5% copper
                            </li>
                            
                          </ul>
                      </b-tab>
                    </b-tabs>
                  </b-card>
                </b-card-body>
              </b-collapse>
            </b-card>
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-btn block href="#" v-b-toggle.accordion3 variant="info">Bloat : {{sameKembungRules}}%</b-btn>
              </b-card-header>
              <b-collapse id="accordion3" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                 <b-card no-body>
                    <b-tabs>
                      <b-tab active>
                          <template slot="title">
                            <strong>Symptoms summary</strong>
                          </template>
                         <b-table striped outlined stacked="sm" hover :items="tableItems" :fields="tableFields" head-variant="light">
                          <div slot="key-question" slot-scope="data">
                            {{data.item.question}}
                           
                          </div>
                          <div slot="key-answer" slot-scope="data">
                            
                            <b-badge :variant="getStatus(data.item.answer)">{{questionStatus}}</b-badge>
                          </div>
                          </b-table>
                      </b-tab>
                      <b-tab>
                          <template slot="title">
                            <strong>Prevention advice</strong>
                          </template>
                        <ul>
                          <li>
                            Give rations in the form of seeds in stages
                          </li>
                          
                        </ul>
                      </b-tab>
                       <b-tab>
                          <template slot="title">
                            <strong>Treatment advice</strong>
                          </template>
                        <ul>
                          <li>
                            Giving drug bloat magnesium oxide solution, which is 500 ml of coconut oil and vegetable oil liquid which is given intrarumina
                          </li>
                        </ul>
                      </b-tab>
                    </b-tabs>
                  </b-card>
                </b-card-body>
              </b-collapse>
            </b-card>
          </div>
          <table style="float:right">
            <tr>
              <td>
                  <b-btn v-if="tabIndex > 0" class="mt-4" variant="warning" @click="prev">Previous</b-btn>      
              </td>
              <td>
                  <b-btn v-if="tabIndex < progress_max-1" class="mt-4" id="asd"  variant="warning" @click="clicked">Next Step</b-btn>
                  <b-btn v-if="progress_max+1 < tabIndex+3" class="mt-4" id="asd2"  variant="danger" @click="doDiagnose">Diagnose</b-btn>
              
              </td>
              </tr>
          </table>
           
          
          
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
      mastitisRules:["1","1","1","1","0","0","0","0","0","0"],
      footrootRules:["1","0","0","0","1","1","1","0","0","0"],
      kembungRules:["1","0","0","0","0","0","0","1","1","1"],
      sameMastitisRules:0,
      sameFootrootRules:0,
      sameKembungRules:0,
      text:"dsadasdsdsd",
      
      max2: 50,
      value: 33.333333333,
      value3: 75,
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
      
    },
    getStatus(tmp){
      
      var kondisiPointer = 0;
      if(Number(tmp) == 0 ){
        this.questionStatus="No";
      }else{
        kondisiPointer = 1;
        this.questionStatus="Yes";
      }
      return kondisiPointer == 0 ? 'danger' : 'success'
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
      if(this.progress_counter == 0){
        this.tabIndex = 0;
        this.progress_counter = 0;
      }else{
        this.tabIndex--;
        this.progress_counter--;
      }
      
    },
    doDiagnose(){
      if(this.progress_counter == this.progress_max){
        // console.log("max===")
        this.progress_counter = this.progress_max
      }else{
        this.progress_counter++
      }
      console.log(this.userResponses)
    }
  }
}
</script>

