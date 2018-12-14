<template>
  <div class="animated fadeIn">
    <b-row>
        <b-col lg="12" md="12">
            <div class="brand-card">
              <div class="brand-card-header bg-linkedin">
               <img src="img/cow/cow (2).png" width="50px" alt="CoreUI Logo"> <h1>{{nameOfCow}}</h1>
              </div>
              <div class="brand-card-body">
                <div>
                  <div class="text-value">{{currentTemp}}</div>
                  <div class="text-uppercase text-muted small">Celcius</div>
                </div>
                <div>
                  <div class="text-value">{{currentHeart}}</div>
                  <div class="text-uppercase text-muted small">BPM</div>
                </div>
              </div>
            </div>
        </b-col>
    </b-row>
    <b-row>
      <b-col md="12">
        <b-card header="History List">

    <b-card>
      <b-row>
        <b-col sm="5">
          <h4 id="traffic" class="card-title mb-0">Traffic</h4>
          <div class="small text-muted">November 2017</div>
        </b-col>
        <b-col sm="7" class="d-none d-md-block">
          <b-button type="button" variant="primary" class="float-right"><i class="icon-cloud-download"></i></b-button>
          <b-button-toolbar class="float-right" aria-label="Toolbar with buttons group">
            <b-form-radio-group class="mr-3" id="radiosBtn" buttons button-variant="outline-secondary" v-model="selected" name="radiosBtn">
              <b-form-radio class="mx-0" value="Day">Day</b-form-radio>
              <b-form-radio class="mx-0" value="Month">Month</b-form-radio>
              <b-form-radio class="mx-0" value="Year">Year</b-form-radio>
            </b-form-radio-group>
          </b-button-toolbar>
        </b-col>
      </b-row>
      <main-chart-example chartId="main-chart-01" class="chart-wrapper" style="height:300px;margin-top:40px;" height="300"></main-chart-example>
      <div slot="footer">
        <b-row class="text-center">
          <b-col class="mb-sm-2 mb-0">
            <div class="text-muted">Visits</div>
            <strong>29.703 Users (40%)</strong>
            <b-progress height={} class="progress-xs mt-2" :precision="1" variant="success" :value="40"></b-progress>
          </b-col>
          <b-col class="mb-sm-2 mb-0 d-md-down-none">
            <div class="text-muted">Unique</div>
            <strong>24.093 Users (20%)</strong>
            <b-progress height={} class="progress-xs mt-2" :precision="1" variant="info" :value="20"></b-progress>
          </b-col>
          <b-col class="mb-sm-2 mb-0">
            <div class="text-muted">Pageviews</div>
            <strong>78.706 Views (60%)</strong>
            <b-progress height={} class="progress-xs mt-2" :precision="1" variant="warning" :value="60"></b-progress>
          </b-col>
          <b-col class="mb-sm-2 mb-0">
            <div class="text-muted">New Users</div>
            <strong>22.123 Users (80%)</strong>
            <b-progress height={} class="progress-xs mt-2" :precision="1" variant="danger" :value="80"></b-progress>
          </b-col>
          <b-col class="mb-sm-2 mb-0 d-md-down-none">
            <div class="text-muted">Bounce Rate</div>
            <strong>Average Rate (40.15%)</strong>
            <b-progress height={} class="progress-xs mt-2" :precision="1" :value="40"></b-progress>
          </b-col>
        </b-row>
      </div>
    </b-card>
          <b-row>
            <b-table striped outlined stacked="sm" hover :items="tableItems" :fields="tableFields" head-variant="light">
           
            <div slot="key-kondisi" slot-scope="data">
              <b-badge :variant="getKondisi(data.item.kondisi)">{{CurrentConditions}}</b-badge>
            </div>
            
            <div slot="key-suhu" slot-scope="data">
              
              <strong>{{data.item.suhu.toFixed(2)}}</strong>
              <div class="small text-muted">Celcius</div>
            </div>
            <div slot="key-jantung" slot-scope="data">
              
              <strong>{{data.item.jantung.toFixed(2)}}</strong>
              <div class="small text-muted">BPM</div>
            </div>
             <div slot="key-tanggal" slot-scope="data">
              <b-badge :variant="dateFormatter(data.item.tanggal)">{{dateOnFormat}}</b-badge>
              
            </div>
            
          </b-table>
          <!-- <b-row>
            <b-col md="6" class="my-1">
              <b-pagination :total-rows="totalRows" :per-page="perPage" v-model="currentPage" class="my-0" />
            </b-col>
          </b-row> -->
          </b-row>
        </b-card>
      </b-col>
    </b-row>
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
import PostsService from "@/services/PostsService";

export default {
  name: 'Details',
  components: {
    Callout,
    // myComponent,
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
      nameOfCow:"",
      socket : io('206.189.36.70:3001'),
      CurrentConditions:"",
      dateOnFormat:"",
      currentTemp:0,
      currentHeart:0,
      tableItems: [],
      tableFields: [
        
        {
          key:'key-kondisi',
          label:'Condition'
        },
        { key: 'key-suhu', 
          label: 'Temperature' 
        },
        { key: 'key-jantung', 
          label: 'Heart Rate' 
        },
        { key: 'key-tanggal', 
          label: 'Time' 
        }
      ],
      // currentPage: 1,
      // perPage: 5,
      // totalRows: this.tableItems.length,
      // pageOptions: [ 5, 10, 15 ]
      // DeviceActive:0,
      // DeviceNonActive:0,
      // TemperatureAverage:0,
      // HeartRateAverage:0,
      // TemperatureGraph:[0, 23, 56, 22, 97,100,100],
      // CurrentConditions:"",
      // suhuArrange:[],
      // statusDeviceInStr:"",
      // dateOnFormat:"",
      // sapiList:[],
      selected: 'Month',
      // tableItems: [],
      // tableFields: [
      //   {
      //     key:'namaSapi',
      //     label: 'Cow ID'
          
      //   },
      //   {
      //     key:'key-kondisi',
      //     label:'Current Condition'
      //   },
      //   { key: 'key-tanggal', 
      //     label: 'Time' 
      //   },
      //   { key: 'key-suhu', 
      //     label: 'Temperature' 
      //   },
      //   { key: 'key-jantung', 
      //     label: 'Heart Rate' 
      //   },
      //   { key: 'key-status', 
      //     label: 'Device Status'
      //   },
      //   {
      //     key: 'key-action',
      //     label: 'Actions'
      //   }
      // ]
    }
  },
  created(){
      // setInterval(function () {
      //   this.getds();
      // }.bind(this), 60000);
      // setInterval(function () { 
      //   this.getds();
      // }.bind(this), 25000);
      this.checkSession(); 
  },
  methods: {
     checkSession(){
      // window.localStorage.removeItem("token")
      if(window.localStorage.getItem("token") == null){
        this.$router.push({ name: 'Login' })  
      }else{
        this.firstLoad();
      }
    },
    async fetchDataSapi(){
      const response = await PostsService.getSapiDetail(window.localStorage.getItem("token"),this.$route.params.id);
      return response.data;
    },
    soket(){
      this.socket.on('/topic/cows/detail/'+this.$route.params.id, (sapiData) => {
        this.nameOfCow = sapiData.namaSapi;
        this.tableItems = sapiData.perangkat.data;
        this.currentTemp = sapiData.perangkat.data[sapiData.perangkat.data.length-1].suhu.toFixed(2);
        this.currentHeart = sapiData.perangkat.data[sapiData.perangkat.data.length-1].jantung.toFixed(2);
      })
    },
    
    async firstLoad(){
      const response = await this.fetchDataSapi();
      let sapiData = response.sapi;
      this.nameOfCow = sapiData.namaSapi;
      this.tableItems = sapiData.perangkat.data;
      this.currentTemp = sapiData.perangkat.data[sapiData.perangkat.data.length-1].suhu.toFixed(2);
      this.currentHeart = sapiData.perangkat.data[sapiData.perangkat.data.length-1].jantung.toFixed(2);
      this.soket();
    },
    getBadge (status) {
      if(status==0){
        this.statusDeviceInStr="Nonactive";
      }else{
        this.statusDeviceInStr="Active";
      }
      return status == 0 ? 'danger' : 'success'
    },
    getKondisi(tmp){
      
      var kondisiPointer = 0;
      if(Number(tmp) == 0 ){
        this.CurrentConditions="Upnormal";
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
    toDetail (id){
       this.$router.push({ name: 'Details', params: {id : id} })
      console.log(id);
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
  .header-section{
    text-align: center;
  }
</style>
