<template>
  <div class="wrapper">
    <div class="animated fadeIn">
      <b-row>
        <b-col lg="12" md="12">
          <!-- show-progress -->
          <b-progress :value="counter" variant="warning" :max="max" animated></b-progress>
           
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
          <b-tabs pills v-model="tabIndex">
            <b-tab >
              <h3>Does cow not appetite ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans1_1" name="ans1" class="custom-control-input" value="1" v-model="ans1">
                    <label class="custom-control-label" for="ans1_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans1_2" name="ans1" class="custom-control-input" value="0" v-model="ans1">
                    <label class="custom-control-label" for="ans1_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
            <b-tab>
               <h3>Does milk production decrease ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans2_1" name="ans2" class="custom-control-input" value="1" v-model="ans2">
                    <label class="custom-control-label" for="ans2_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans2_2" name="ans2" class="custom-control-input" value="0" v-model="ans2">
                    <label class="custom-control-label" for="ans2_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
            <b-tab >
               <h3>Does milk change ? e.g colour</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                 
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans3_1" name="ans3" class="custom-control-input" value="1" v-model="ans3">
                    <label class="custom-control-label" for="ans3_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans3_2" name="ans3" class="custom-control-input" value="0" v-model="ans3">
                    <label class="custom-control-label" for="ans3_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
            <b-tab>
               <h3>Does mammary glands swollen ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                 
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans4_1" name="ans4" class="custom-control-input" value="1" v-model="ans4">
                    <label class="custom-control-label" for="ans4_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans4_2" name="ans4" class="custom-control-input" value="0" v-model="ans4">
                    <label class="custom-control-label" for="ans4_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
            <b-tab>
               <h3>Does the cow limp ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                 
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans5_1" name="ans5" class="custom-control-input" value="1" v-model="ans5">
                    <label class="custom-control-label" for="ans5_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans5_2" name="ans5" class="custom-control-input" value="0" v-model="ans5">
                    <label class="custom-control-label" for="ans5_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
            <b-tab>
               <h3>Does the nail gap appear red ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                 
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans6_1" name="ans6" class="custom-control-input" value="1" v-model="ans6">
                    <label class="custom-control-label" for="ans6_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans6_2" name="ans6" class="custom-control-input" value="0" v-model="ans6">
                    <label class="custom-control-label" for="ans6_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
            <b-tab>
               <h3>Does the gap nail give off a white liquid ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                 
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans7_1" name="ans7" class="custom-control-input" value="1" v-model="ans7">
                    <label class="custom-control-label" for="ans7_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans7_2" name="ans7" class="custom-control-input" value="0" v-model="ans7">
                    <label class="custom-control-label" for="ans7_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
             <b-tab>
               <h3>Does the cow stop rumination ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                 
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans8_1" name="ans8" class="custom-control-input" value="1" v-model="ans8">
                    <label class="custom-control-label" for="ans8_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans8_2" name="ans8" class="custom-control-input" value="0" v-model="ans8">
                    <label class="custom-control-label" for="ans8_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
            <b-tab>
               <h3>Does the left side of the stomach look big ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                 
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans9_1" name="ans9" class="custom-control-input" value="1" v-model="ans9">
                    <label class="custom-control-label" for="ans9_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans9_2" name="ans9" class="custom-control-input" value="0" v-model="ans9">
                    <label class="custom-control-label" for="ans9_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
              <b-tab>
               <h3>When the stomach is hit, it sounds like a drum ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                 
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans10_1" name="ans10" class="custom-control-input" value="1" v-model="ans10">
                    <label class="custom-control-label" for="ans10_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans10_2" name="ans10" class="custom-control-input" value="0" v-model="ans10">
                    <label class="custom-control-label" for="ans10_2">No</label>
                  </div>
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
          <b-btn class="mt-4" variant="warning" @click="prev">Previous</b-btn> &nbsp
          <b-btn class="mt-4" id="asd"  variant="warning" @click="clicked">Next Step</b-btn>
          
          
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
export default {
  name: 'expert',
  data () {
    return {
      questionStatus: "",
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
      tabIndex: 0,
      counter: 1,
      max: 10,
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
  methods: {
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
     // console.log("coun"+this.counter+"tab"+this.tabIndex)
      if( this.counter == 10 && this.tabIndex == 9 ){
        // this.tabIndex=10;
        // this.counter=10;
         this.ansArray.push(this.ans1);
         this.ansArray.push(this.ans2);
         this.ansArray.push(this.ans3);
         this.ansArray.push(this.ans4);
         this.ansArray.push(this.ans5);
         this.ansArray.push(this.ans6);
         this.ansArray.push(this.ans7);
         this.ansArray.push(this.ans8);
         this.ansArray.push(this.ans9);
         this.ansArray.push(this.ans10);
         for(var i=0;i<this.ansArray.length;i++){
           if(this.ansArray[i] == this.mastitisRules[i]){
             this.sameMastitisRules++;
           }
           if(this.ansArray[i] == this.footrootRules[i]){
             this.sameFootrootRules++;
           }
           if(this.ansArray[i] == this.kembungRules[i]){
             this.sameKembungRules++;
           }
         }
         this.sameMastitisRules = (this.sameMastitisRules/10)*100;
         this.sameFootrootRules = (this.sameFootrootRules/10)*100;
         this.sameKembungRules = (this.sameKembungRules/10)*100;
         const items = [
            { question: 'Cow not appetite', answer: this.ansArray[1] },
            { question: 'Milk production decrease', answer: this.ansArray[2] },
            { question: 'Milk change,e.g colour', answer: this.ansArray[3] },
            { question: 'Mammary glands swollen', answer: this.ansArray[4] },
            { question: 'The cow limp', answer: this.ansArray[5] },
            { question: 'The nail gap appear red', answer: this.ansArray[6] },
            { question: 'The gap nail give off a white liquid', answer: this.ansArray[7] },
            { question: 'The cow stop rumination', answer: this.ansArray[8] },
            { question: 'The left side of the stomach look big', answer: this.ansArray[9] },
            { question: 'When the stomach is hit, it sounds like a drum', answer: this.ansArray[10] }
          ]
         this.tableItems = items;
        //  console.log("mastitis : "+this.sameMastitisRules);
        //  console.log("footroot : "+this.sameFootrootRules);
        //  console.log("kembung : "+this.sameKembungRules);
      }else{
        this.tabIndex++;
        this.counter++;
      }
      
      
    },
    prev () {
      if(this.tabIndex == 0 && this.counter == 1 ){
        this.tabIndex=0;
        this.counter=1;
      }else{
        this.tabIndex--;
        this.counter--;
      }
      
    }
  },
  mounted () {
    // this.timer = setInterval(() => {
    //   this.bars.forEach(bar => {
    //     bar.value = 25 + (Math.random() * 75)
    //   })
    // }, 2000)
  },
  // beforeDestroy () {
  //   clearInterval(this.timer)
  //   this.timer = null
  // }
}
</script>

