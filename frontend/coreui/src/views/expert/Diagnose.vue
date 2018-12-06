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
          <b-tabs pills v-model="tabIndex">
            <b-tab >
              <h3>Apakah Sapi terlihat mabuk ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans1_1" name="ans1" class="custom-control-input" value="1">
                    <label class="custom-control-label" for="ans1_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans1_2" name="ans1" class="custom-control-input" value="2">
                    <label class="custom-control-label" for="ans1_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
            <b-tab>
               <h3>Apakah Sapi terlihat mabuk ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans2_1" name="ans2" class="custom-control-input" value="1">
                    <label class="custom-control-label" for="ans2_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans2_2" name="ans2" class="custom-control-input" value="2">
                    <label class="custom-control-label" for="ans2_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
            <b-tab >
               <h3>Apakah Sapi terlihat mabuk ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                 
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans3_1" name="ans3" class="custom-control-input" value="1">
                    <label class="custom-control-label" for="ans3_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans3_2" name="ans3" class="custom-control-input" value="2">
                    <label class="custom-control-label" for="ans3_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
            <b-tab>
               <h3>Apakah Sapi terlihat mabuk ?</h3>
              <br>
              <b-form-group :label-cols="0" :horizontal="true">
                <b-form-radio-group
                 
                  stacked>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans4_1" name="ans4" class="custom-control-input" value="1">
                    <label class="custom-control-label" for="ans4_1">Yes</label>
                  </div>
                  <div class="custom-control custom-radio">
                    <input type="radio" id="ans4_2" name="ans4" class="custom-control-input" value="2">
                    <label class="custom-control-label" for="ans4_2">No</label>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </b-tab>
          </b-tabs>
          <b-btn class="mt-4" variant="warning" @click="prev">Previous</b-btn> &nbsp
          <b-btn class="mt-4"  variant="warning" @click="clicked">Next</b-btn>
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
      tabIndex: 0,
      counter: 1,
      max: 4,
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
    clicked () {
      if(this.tabIndex == 4 && this.counter == 4 ){
        this.tabIndex=4;
        this.counter=4;
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
    this.timer = setInterval(() => {
      this.bars.forEach(bar => {
        bar.value = 25 + (Math.random() * 75)
      })
    }, 2000)
  },
  beforeDestroy () {
    clearInterval(this.timer)
    this.timer = null
  }
}
</script>

