<template>
<div>
    <bounce-spinner v-if="isLoading"></bounce-spinner>
  <div class="animated fadeIn" v-if="isLoading==false">
  
    <b-row>
      <b-alert show variant="success" v-if="successAlert.length > 0">
              <h4 class="alert-heading">Congratulation !</h4>
              <ul>
                <li v-for="item in successAlert" :key="item">{{ item }}</li>
              </ul>
              
      </b-alert>
      <b-col sm="6" lg="6">
        <b-card  bg-variant="info" text-variant="white">
          <h1 class="card-text">
            {{DeviceActive}} 
          </h1>
          <p>Active Device</p>
        </b-card>
        <!-- <b-card no-body class="bg-info">
          <b-card-body class="pb-0">
            <b-dropdown class="float-right" variant="transparent p-0" right >
              <template slot="button-content">
                <i class="icon-settings"></i>
              </template>
              <b-dropdown-item>Action</b-dropdown-item>
              <b-dropdown-item>Another action</b-dropdown-item>
              <b-dropdown-item>Something else here...</b-dropdown-item>
              <b-dropdown-item disabled>Disabled action</b-dropdown-item>
            </b-dropdown>
             <span>coba: {{ incr }}</span>
            <my-component title={{statusDevice[0]}} ></my-component>
            <p>Active Device</p>
          </b-card-body>
          <card-line2-chart-example chartId="card-chart-02" class="chart-wrapper px-3" style="height:70px;" :height="70"/>
        </b-card> -->
      </b-col>
      <b-col sm="6" lg="6">
        <b-card  bg-variant="danger" text-variant="white">
          <h1 class="card-text">
            {{DeviceNonActive}}
          </h1>
          <p>Nonactive Device</p>
        </b-card>
        <!-- <b-card no-body class="bg-danger">
          <b-card-body class="pb-0">
            <b-dropdown class="float-right" variant="transparent p-0" right>
              <template slot="button-content">
                <i class="icon-settings"></i>
              </template>
              <b-dropdown-item>Action</b-dropdown-item>
              <b-dropdown-item>Another action</b-dropdown-item>
              <b-dropdown-item>Something else here...</b-dropdown-item>
              <b-dropdown-item disabled>Disabled action</b-dropdown-item>
            </b-dropdown>
            <h1 class="mb-0">{{statusDevice[1]}}</h1>
            <p>Nonactive Device</p>
          </b-card-body>
          <card-bar-chart-example chartId="card-chart-04" class="chart-wrapper px-3" style="height:70px;" height="70"/>
        
        </b-card> -->
      </b-col>
    </b-row>

    <!-- <b-row>
      <b-col sm="12" lg="12" >
        <div class="brand-card" v-for="item in sapiList" :key="item._id">
          <div class="brand-card-header">
            <img src="img/cow/cow (3).png" width="5%" alt="CoreUI Logo">
           
            <h1 class="list-sapi-header">{{item.namaSapi}}</h1>
              <div class="float-right">
                  <small class="text-muted">{{item.perangkat.data[item.perangkat.data.length-1].tanggal}}</small>
              </div>
            <template slot="status" slot-scope="data">
              <b-badge :variant="getBadge(item.perangkat.status)">{{item.perangkat.status}}</b-badge>
            </template>
            <div class="chart-wrapper">
              
              <social-box-chart-example chartId="box-chart-01" :data="[65, 59, 84, 84, 51, 55, 40]" />
            </div>
          </div>
          <div class="brand-card-body">
            <div>
              <div class="text-value">
                <b-badge :variant="getBadge(item.perangkat.status)">{{statusDeviceInStr}}</b-badge>
              </div>
              <div class="text-uppercase text-muted small">{{item.perangkat.data[item.perangkat.data.length-1].tanggal}}</div>
            </div> 
            <div>
              <div class="text-value">{{item.perangkat.data[item.perangkat.data.length-1].suhu}}</div>
              <div class="text-uppercase text-muted small">Celcius</div>
            </div>
            <div>
              <div class="text-value">{{item.perangkat.data[item.perangkat.data.length-1].jantung}}</div>
              <div class="text-uppercase text-muted small">Beats per-minutes</div>
            </div>
            
          </div>
         
        </div>
      </b-col>
      
    </b-row> -->
    <b-row>
      <b-col md="12">
        <b-card header="Cow List" class="card-accent-warning">
           <div slot="header">
              <b>Cow List</b>
              <div class="card-header-actions">
                <b-button type="button" variant="warning" @click="showModal" class="mr-1">Register Cow</b-button>
                <!-- <b-link @click="warningModal = true" class="card-header-action btn-setting">
                   <i class="icon-plus icons font-2xl d-block mt-4"></i>
                </b-link>
                <b-link class="card-header-action btn-minimize" v-b-toggle.collapse1>
                  <i class="icon-arrow-up"></i>
                </b-link>
                <b-link href="#" class="card-header-action btn-close" v-on:click="show = !show">
                  <i class="icon-close"></i>
                </b-link> -->
              </div>
          </div>
          <b-row>        
             <b-col sm="12" lg="12">
              <b-row v-if="existingData == true">
                <b-col sm="6">
                  <Callout variant="info">
                    <b-row>
                      <b-col sm="12" lg="6">
                        <small class="text-muted">Temperature Average</small><br>
                        <strong class="h4">{{ TemperatureAverage }}</strong>
                      </b-col>
                      <b-col sm="12" lg="6">
                    <!-- <div class="chart-wrapper"> -->
                      <!--<callout-chart-example :data="[35, 23, 56, 22, 97, 23, 64]" variant="#20a8d8" width="80" height="30" />-->
                        <callout-chart-example chartId="callout-chart-01" :labels="labelsData" :data="TemperatureGraph" variant="info" width="80" height="30" />
                    <!-- </div> -->
                      </b-col>
                    </b-row>
                  </Callout>
                </b-col>
                <b-col sm="6">
                  <Callout variant="danger">
                    <b-row>
                      <b-col sm="12" lg="6">
                        <small class="text-muted">Heart Rate Average</small><br>
                        <strong class="h4">{{HeartRateAverage}}</strong>
                      </b-col>
                      <b-col sm="12" lg="6">
                        <!-- <div class="chart-wrapper"> -->
                        <callout-chart-example chartId="callout-chart-02" :labels="labelsData" :data="HeartGraph" variant="danger" width="80" height="30" />
                        <!-- </div> -->
                      </b-col>
                    </b-row>
                  </Callout>
                </b-col>
              </b-row>
              <hr class="mt-0">
             </b-col>
          </b-row>
          <b-row>
            <b-table striped outlined stacked="sm" hover :items="tableItems" :fields="tableFields" head-variant="light"  v-if="existingData == true">
            <div slot="namaSapi" slot-scope="data">
              <img src="img/cow/cow (2).png" width="50px" alt="cows logo">
              <strong>{{data.value}}</strong>
              <b-link class="card-header-action btn-minimize" v-b-toggle.collapse1>
                  <i v-bind:id="data.item._id" class="icon-eye"></i>
              </b-link>
              <b-popover v-bind:target="data.item._id" title="Cow ID">
                <!-- <strong>{{data.item._id}}</strong> -->
                <h5><b-badge variant="secondary">{{data.item.perangkat.idOnRaspi}}</b-badge></h5>
              </b-popover>
              <!-- <div class="small text-muted">{{data.item._id}}</div> -->
            </div>
            <div slot="key-kondisi" slot-scope="data">
              <b-badge :variant="getKondisi(data.item.perangkat.data[data.item.perangkat.data.length-1].kondisi)">{{CurrentConditions}}</b-badge>
            </div>
            <div slot="key-tanggal" slot-scope="data">
              <b-badge :variant="dateFormatter(data.item.perangkat.data[data.item.perangkat.data.length-1].tanggal)">{{dateOnFormat}}</b-badge>
              
            </div>
            <div slot="key-suhu" slot-scope="data">
              
              <strong>{{data.item.perangkat.data[data.item.perangkat.data.length-1].suhu.toFixed(2)}}</strong>
              <div class="small text-muted">Celcius</div>
            </div>
            <div slot="key-jantung" slot-scope="data">
              
              <strong>{{data.item.perangkat.data[data.item.perangkat.data.length-1].jantung.toFixed(2)}}</strong>
              <div class="small text-muted">BPM</div>
            </div>
            <div slot="key-status" slot-scope="data">
              <b-badge :variant="getBadge(data.item.perangkat.status)">{{statusDeviceInStr}}</b-badge>
            </div>
            <div slot="key-action" slot-scope="data">
              <b-button variant="primary" size="sm" @click="toDetail(data.item._id)">Show Details</b-button>
            </div>
            <div slot="key-expert" slot-scope="data">
              <b-button variant="success" size="sm" @click="toExpert(data.item._id)">Identification</b-button>
            </div>
          </b-table> 
            
          </b-row> 
            <b-alert v-if="existingData == false" show variant="warning">
              You don't have a cow in our system, let's manage your first cow by clicking the register cow button.
            </b-alert>
        </b-card>
      </b-col>
    </b-row>
          
    <b-modal variant="warning" class="modal-warning"  ref="myModalRef" hide-footer title="Register">
      <div class="d-block text-center">
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
        <b-form-group>
          <b-form-input type="text" id="name" v-model="cowName" placeholder="Enter your cow ID or name"></b-form-input>
        </b-form-group>
      </div>
      <b-btn class="mt-3" variant="outline-warning" block @click="createCow">Register</b-btn>
    </b-modal>

    <!-- <b-row>
      <b-col md="12">
        <b-card header="Traffic &amp; Sales">
          <b-row>
            <b-col sm="12" lg="6">
              <b-row>
                <b-col sm="6">
                  <Callout variant="info">
                    <small class="text-muted">New Clients</small><br>
                    <strong class="h4">9,123</strong>
                    <div class="chart-wrapper" :style="{ top: '-10px'}">
                      <callout-chart-example :data="[35, 23, 56, 22, 97, 23, 64]" variant="#20a8d8" width="80" height="30" />
                      <callout-chart-example chartId="callout-chart-01" :data="[35, 23, 56, 22, 97, 23, 64]" variant="info" width="80" height="30" />
                    </div>
                  </Callout>
                </b-col>
                <b-col sm="6">
                  <Callout variant="danger">
                    <small class="text-muted">Recurring Clients</small><br>
                    <strong class="h4">22,643</strong>
                    <div class="chart-wrapper" :style="{ top: '-10px'}">
                      <callout-chart-example chartId="callout-chart-02" :data="[65, 59, 84, 84, 51, 55, 40]" variant="danger" width="80" height="30" />
                    </div>
                  </Callout>
                </b-col>
              </b-row>
              <hr class="mt-0">
              <div class="progress-group mb-4">
                <div class="progress-group-prepend">
                  <span class="progress-group-text">
                    Monday
                  </span>
                </div>
                <div class="progress-group-bars">
                  <b-progress class="progress-xs" variant="info" :value="34" height={} />
                  <b-progress class="progress-xs" variant="danger" :value="78" height={} />
                </div>
              </div>
              <div class="progress-group mb-4">
                <div class="progress-group-prepend">
                  <span class="progress-group-text">
                    Tuesday
                  </span>
                </div>
                <div class="progress-group-bars">
                  <b-progress height={} class="progress-xs" :value="56" variant="info"></b-progress>
                  <b-progress height={} class="progress-xs" :value="94" variant="danger"></b-progress>
                </div>
              </div>
              <div class="progress-group mb-4">
                <div class="progress-group-prepend">
                  <span class="progress-group-text">
                    Wednesday
                  </span>
                </div>
                <div class="progress-group-bars">
                  <b-progress height={} class="progress-xs" :value="12" variant="info"></b-progress>
                  <b-progress height={} class="progress-xs" :value="67" variant="danger"></b-progress>
                </div>
              </div>
              <div class="progress-group mb-4">
                <div class="progress-group-prepend">
                  <span class="progress-group-text">
                    Thursday
                  </span>
                </div>
                <div class="progress-group-bars">
                  <b-progress height={} class="progress-xs" :value="43" variant="info"></b-progress>
                  <b-progress height={} class="progress-xs" :value="91" variant="danger"></b-progress>
                </div>
              </div>
              <div class="progress-group mb-4">
                <div class="progress-group-prepend">
                  <span class="progress-group-text">
                    Friday
                  </span>
                </div>
                <div class="progress-group-bars">
                  <b-progress height={} class="progress-xs" :value="22" variant="info"></b-progress>
                  <b-progress height={} class="progress-xs" :value="73" variant="danger"></b-progress>
                </div>
              </div>
              <div class="progress-group mb-4">
                <div class="progress-group-prepend">
                  <span class="progress-group-text">
                    Saturday
                  </span>
                </div>
                <div class="progress-group-bars">
                  <b-progress height={} class="progress-xs" :value="53" variant="info"></b-progress>
                  <b-progress height={} class="progress-xs" :value="82" variant="danger"></b-progress>
                </div>
              </div>
              <div class="progress-group mb-4">
                <div class="progress-group-prepend">
                  <span class="progress-group-text">
                    Sunday
                  </span>
                </div>
                <div class="progress-group-bars">
                  <b-progress height={} class="progress-xs" :value="9" variant="info"></b-progress>
                  <b-progress height={} class="progress-xs" :value="69" variant="danger"></b-progress>
                </div>
              </div>
              <div class="legend text-center">
                <small>
                  <sup><b-badge pill variant="info">&nbsp;</b-badge></sup>
                  New clients
                  &nbsp;&nbsp;
                  <sup><b-badge pill variant="danger">&nbsp;</b-badge></sup>
                  Recurring clients
                </small>
              </div>
            </b-col>
            <b-col sm="12" lg="6">
              <b-row>
                <b-col sm="6">
                  <Callout variant="warning">
                    <small class="text-muted">Pageviews</small><br>
                    <strong class="h4">78,623</strong>
                    <div class="chart-wrapper" :style="{ top: '-10px'}">
                      <callout-chart-example chartId="callout-chart-03" :data="[35, 23, 56, 22, 97, 23, 64]" variant="#f8cb00" width="80" height="30"/>
                    </div>
                  </Callout>
                </b-col>
                <b-col sm="6">
                  <Callout variant="success">
                    <small class="text-muted">Organic</small><br>
                    <strong class="h4">49,123</strong>
                    <div class="chart-wrapper" :style="{ top: '-10px'}">
                      <callout-chart-example chartId="callout-chart-04" :data="[65, 59, 84, 84, 51, 55, 40]" variant="#4dbd74" width="80" height="30" />
                    </div>
                  </Callout>
                </b-col>
              </b-row>
              <hr class="mt-0">
              <ul class="horizontal-bars type-2">
                <div class="progress-group">
                  <div class="progress-group-header">
                    <i class="icon-user progress-group-icon"></i>
                    <span class="title">Male</span>
                    <span class="ml-auto font-weight-bold">43%</span>
                  </div>
                  <div class="progress-group-bars">
                    <b-progress height={} class="progress-xs" :value="43" variant="warning"></b-progress>
                  </div>
                </div>
                  <div class="progress-group-header">
                <div class="progress-group mb-5">
                    <i class="icon-user-female progress-group-icon"></i>
                    <span class="title">Female</span>
                    <span class="ml-auto font-weight-bold">37%</span>
                  </div>
                  <div class="progress-group-bars">
                    <b-progress height={} class="progress-xs" :value="37" variant="warning"></b-progress>
                  </div>
                </div>
                <div class="progress-group">
                  <div class="progress-group-header">
                    <i class="icon-globe progress-group-icon"></i>
                    <span class="title">Organic Search</span>
                    <span class="ml-auto font-weight-bold">191,235 <span class="text-muted small">(56%)</span></span>
                  </div>
                  <div class="progress-group-bars">
                    <b-progress height={} class="progress-xs" :value="56" variant="success"></b-progress>
                  </div>
                </div>
                <div class="progress-group">
                  <div class="progress-group-header">
                    <i class="icon-social-facebook progress-group-icon"></i>
                    <span class="title">Facebook</span>
                    <span class="ml-auto font-weight-bold">51,223 <span class="text-muted small">(15%)</span></span>
                  </div>
                  <div class="progress-group-bars">
                    <b-progress height={} class="progress-xs" :value="15" variant="success"></b-progress>
                  </div>
                </div>
                <div class="progress-group">
                  <div class="progress-group-header">
                    <i class="icon-social-twitter progress-group-icon"></i>
                    <span class="title">Twitter</span>
                    <span class="ml-auto font-weight-bold">37,564 <span class="text-muted small">(11%)</span></span>
                  </div>
                  <div class="progress-group-bars">
                    <b-progress height={} class="progress-xs" :value="11" variant="success"></b-progress>
                  </div>
                </div>
                <div class="progress-group">
                  <div class="progress-group-header">
                    <i class="icon-social-linkedin progress-group-icon"></i>
                    <span class="title">LinkedIn</span>
                    <span class="ml-auto font-weight-bold">27,319 <span class="text-muted small">&nbsp;(8%)</span></span>
                  </div>
                  <div class="progress-group-bars">
                    <b-progress height={} class="progress-xs" :value="8" variant="success"></b-progress>
                  </div>
                </div>
                <div class="divider text-center">
                  <b-button variant="link" size="sm" class="text-muted"><i class="icon-options"></i></b-button>
                </div>
              </ul>
            </b-col>
          </b-row>
          <br/>
        </b-card>
      </b-col>
    </b-row> -->
  </div>
</div>
</template>

<script>
import CardLine1ChartExample from './dashboard/CardLine1ChartExample'
import CardLine2ChartExample from './dashboard/CardLine2ChartExample'
import CardLine3ChartExample from './dashboard/CardLine3ChartExample'
import CardBarChartExample from './dashboard/CardBarChartExample'
import MainChartExample from './dashboard/MainChartExample'
import SocialBoxChartExample from './dashboard/SocialBoxChartExample'
import CalloutChartExample from './dashboard/CalloutChartExample'
import { Callout } from '@coreui/vue'
import io from 'socket.io-client'
import PostsService from "@/services/PostsService"
import Constants from "@/services/Constants"
import 'vue-spinners/dist/vue-spinners.css'
import { BounceSpinner } from 'vue-spinners/dist/vue-spinners.common'


export default {
  name: 'dashboard',
  components: {
    Callout,
    // myComponent,
    BounceSpinner,
    CardLine1ChartExample,
    CardLine2ChartExample,
    CardLine3ChartExample,
    CardBarChartExample,
    MainChartExample,
    SocialBoxChartExample,
    CalloutChartExample
  },
  data() {
    return {
      isLoading: true,
      DeviceActive:0,
      cowName:"",
      socket : io(Constants.SOCKET_SERVER),
      warningModal: false,
      DeviceNonActive:0,
      TemperatureAverage:0,
      HeartRateAverage:0,
      TemperatureGraph:[],
      HeartGraph:[],
      labelsData:[],
      CurrentConditions:"",
      suhuArrange:[],
      statusDeviceInStr:"",
      dateOnFormat:"",
      dateOnFormatForAvg:"",
      existingData:false,
      sapiList:[],
      selected: 'Month',
      tableItems: [],
      errors: [],
      successAlert: [],
      tableFields: [
        {
          key:'namaSapi',
          label: 'Cow ID'
          
        },
        {
          key:'key-kondisi',
          label:'Current Condition'
        },
        { key: 'key-tanggal', 
          label: 'Time' 
        },
        { key: 'key-suhu', 
          label: 'Temperature' 
        },
        { key: 'key-jantung', 
          label: 'Heart Rate' 
        },
        { key: 'key-status', 
          label: 'Device Status'
        },
        {
          key: 'key-action',
          label: 'Details'
        },
        {
          key: 'key-expert',
          label: 'Diagnose'
        }
      ]
    }
  },
  created(){
      this.checkSession();
     
  },
  methods: {
    showModal () {
      /**
       * this function for show create cow form on modal
       */
      this.errors = []
      this.$refs.myModalRef.show()
    },
    async postCreateCowData() {
      /**
       * post create cow data
       */
      this.successAlert = []
      const response = await PostsService.createCow(window.localStorage.getItem("token"),{
                          namaSapi: this.cowName
                        });
      this.$refs.myModalRef.hide()
      if(response.data.status){
        this.successAlert.push('Congratulation,You have successfully register a new cow, our team will prepare your device, please refresh this page');
      }
      // setTimeout(location.reload(), 5000)
      
    },
    createCow() {
      /**
       * this function for action when register cow button on clik
       */
      if(this.cowName){
        
        this.postCreateCowData()
      }
      this.errors = []
      if(!this.cowName){
        this.errors.push('cow ID cant blank !');
      }
     
    },
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
    variant (value) {
      let $variant
      if (value <= 25) {
        $variant = 'info'
      } else if (value > 25 && value <= 50) {
        $variant = 'success'
      } else if (value > 50 && value <= 75) {
        $variant = 'warning'
      } else if (value > 75 && value <= 100) {
        $variant = 'danger'
      }
      return $variant
    },
    flag (value) {
      return 'flag-icon flag-icon-' + value
    },
    async fetchDataSapi(){
      const response = await PostsService.getSapi(window.localStorage.getItem("token"));
      return response.data;
    },
    soket(){
      this.socket.on('/topic/cows/'+window.localStorage.getItem("peternak_id"), (sapiData) => {
            this.tableItems = sapiData;
            var active =0,inActive =0,avgSuhu=0,avgHeart=0;
            for(var i=0;i<sapiData.length;i++){
            avgSuhu += Number(sapiData[i].perangkat.data[sapiData[i].perangkat.data.length-1].suhu);
            avgHeart += Number(sapiData[i].perangkat.data[sapiData[i].perangkat.data.length-1].jantung);
            this.dateFormatter(sapiData[i].perangkat.data[sapiData[i].perangkat.data.length-1].tanggal);
            if(sapiData[i].perangkat.status == 1){
              active++;
            }else{
              inActive++;
            }
          }
          avgSuhu = avgSuhu/sapiData.length;
          avgHeart = avgHeart/sapiData.length;
          this.tableItems = sapiData;
          this.DeviceActive = active;
          this.DeviceNonActive = inActive;
          this.TemperatureAverage = avgSuhu.toFixed(2);
          this.HeartRateAverage = avgHeart.toFixed(2);
          // chart operation
          this.HeartGraph.push(this.HeartRateAverage);
          this.TemperatureGraph.push(this.TemperatureAverage);
          this.labelsData.push(this.dateOnFormat)
            
      });
    },
    async firstLoad(){
      // console.log(window.localStorage.getItem("token"));
      const response = await this.fetchDataSapi();
      let sapiData = response.data;
      this.isLoading=false
      if(sapiData.length > 0){
          this.existingData = true
          var active =0,inActive =0,avgSuhu=0,avgHeart=0;
          for(var i=0;i<sapiData.length;i++){
            avgSuhu += Number(sapiData[i].perangkat.data[sapiData[i].perangkat.data.length-1].suhu);
            avgHeart += Number(sapiData[i].perangkat.data[sapiData[i].perangkat.data.length-1].jantung);
            this.dateFormatter(sapiData[i].perangkat.data[sapiData[i].perangkat.data.length-1].tanggal);
            if(sapiData[i].perangkat.status == 1){
              active++;
            }else{
              inActive++;
            }
          }
          avgSuhu = avgSuhu/sapiData.length;
          avgHeart = avgHeart/sapiData.length;
          this.tableItems = sapiData;
          this.DeviceActive = active;
          this.DeviceNonActive = inActive;
          this.TemperatureAverage = avgSuhu.toFixed(2);
          this.HeartRateAverage = avgHeart.toFixed(2);
          // chart operation
          this.HeartGraph.push(this.HeartRateAverage);
          this.TemperatureGraph.push(this.TemperatureAverage);
          this.labelsData.push(this.dateOnFormat)
          // this.TemperatureGraph = [1,2,3,4,5,6,7]
          // this.labelsData = [1,2,3,4,5,6,7]
          this.soket();
      }else{
        this.existingData=false
      }
      
      // console.log(this.tableItems);
    },
    
    getBadge (status) {
      var varian_='danger'
      if(status==0){
        this.statusDeviceInStr="Nonactive";
      }else if(status==1){
        this.statusDeviceInStr="Active";
        varian_='success'
      }else{
        this.statusDeviceInStr="Pending"
        varian_='secondary'
      }
      // return status == 0 ? 'danger' : 'success'
      return varian_
    },
    getKondisi(tmp){
      
      var kondisiPointer = 0;
      if(Number(tmp) == 0 ){
        this.CurrentConditions="Abnormal";
      }else{
        kondisiPointer = 1;
        this.CurrentConditions="Normal";
      }
      return kondisiPointer == 0 ? 'danger' : 'success'
    },
    dateFormatter(date){
      var created_date = new Date(date);
      var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
      var year = created_date.getFullYear();
      var month = months[created_date.getMonth()];
      var date = created_date.getDate();
      var hour = created_date.getHours();
      var min = created_date.getMinutes();
      var sec = created_date.getSeconds();
      var time = date + ',' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;    // final date with time, you can use this according your requirement
      this.dateOnFormat = time;
      return 'secondary';
    },
    toExpert(id){
      this.$router.push({ name: 'expert', params: {id : id} })
    },
    toDetail (id){
      this.$router.push({ name: 'Details', params: {id : id} })
      
    }
  } 
}
</script>

<style>
  /* IE fix */
  #card-chart-01, #card-chart-02 {
    width: 100% !important;
  }
  .list-sapi-header{
    color:white;
  }
  .brand-card-header{
    background-color: #ffc107 !important;
  }
  .chart-wrapper canvas{
    /* width: 100% !important;  */
    /* margin-top: -10% !important;
    height: 50px !important; */
  }
</style>
