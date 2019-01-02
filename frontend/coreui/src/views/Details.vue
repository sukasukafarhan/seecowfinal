<template>
  <div class="animated fadeIn">
    <!-- <b-row>
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
    </b-row> -->
    <b-row>
      <b-col md="12">
        <b-card header="Monitoring" class="card-accent-warning">
    <b-card>
      <b-row>
        <b-col sm="5">
          <h4><img src="img/cow/cow (2).png" width="50px" alt="CoreUI Logo"> {{nameOfCow}}</h4>
          <!-- <h4 id="traffic" class="card-title mb-0">Graph</h4> -->
          <!-- <div class="small text-muted">{{dateOnFormat}}</div> -->
          <b-badge v-bind:variant="conditions">{{CurrentConditions}}</b-badge> | 
           <b-badge v-bind:variant="statusDevice">{{statusDeviceInStr}}</b-badge> 
        </b-col>
        <b-col sm="7">
          <b-form inline class="float-right">
            <label class="mr-sm-2" for="inlineInput1">Start: </label>
            <b-input id="inlineInput1" type="date" v-model="startDate"></b-input>
            <label class="mx-sm-2" for="inlineInput2">End: </label>
            <b-input id="inlineInput2" type="date" v-model="endDate"></b-input>
            <b-button type="button" variant="primary" class="float-right" @click="filterData"><i class="icon-magnifier"></i></b-button>
          </b-form> 
        </b-col>
      </b-row>
      <line-chart :labels="labelsData" :dataheart="dataChartHeart" :datatemperature="dataChartTemp" :dataheartlimit="dataChartHeartLimit" :datatemperaturelimit="dataChartTemperatureLimit" :temperatureupperlimit="dataChartTemperatureUpperLimit" :heartupperlimit="dataChartHeartUpperLimit" :options="{responsive: true, maintainAspectRatio: false}"></line-chart>
      <div slot="footer">
        <b-row class="text-center">
          <b-col class="mb-sm-6 mb-0">
            <div class="text-muted">Temperature</div>
            <strong>{{currentTemp}}</strong>
             <b-progress height={} class="progress-xs mt-2" :precision="1" v-bind:value="100"></b-progress>
          </b-col>
         
          <b-col class="mb-sm-6 mb-0">
            <div class="text-muted">Heart Rate</div>
            <strong>{{currentHeart}}</strong>
              <b-progress height={} class="progress-xs mt-2" :precision="1" variant="danger" v-bind:value="100"></b-progress>
          </b-col>
          
        </b-row>
      </div>
    </b-card>
             <button v-on:click="changeData">Change data</button>
        </b-card>
      </b-col>
    </b-row>


    <b-row>
      <b-col md="12">
        <b-card header="Monitoring" class="card-accent-warning">
    <b-card>
      <b-row>
        <b-col sm="5">
          <h4 id="traffic" class="card-title mb-0">Graph</h4>
          <div class="small text-muted">{{dateOnFormat}}</div>
        </b-col>
        <b-col sm="7" class="d-none d-md-block">
          <b-button type="button" variant="primary" class="float-right"><i class="icon-cloud-download"></i></b-button>
          <!-- <b-button-toolbar class="float-right" aria-label="Toolbar with buttons group">
            <b-form-radio-group class="mr-3" id="radiosBtn" buttons button-variant="outline-secondary" v-model="selected" name="radiosBtn">
              <b-form-radio class="mx-0" value="Day">Day</b-form-radio>
              <b-form-radio class="mx-0" value="Month">Month</b-form-radio>
              <b-form-radio class="mx-0" value="Year">Year</b-form-radio>
            </b-form-radio-group>
          </b-button-toolbar> -->
        </b-col>
      </b-row>
      <line-chart :labels="labelsData" :dataheart="dataChartHeart" :datatemperature="dataChartTemp" :dataheartlimit="dataChartHeartLimit" :datatemperaturelimit="dataChartTemperatureLimit" :temperatureupperlimit="dataChartTemperatureUpperLimit" :heartupperlimit="dataChartHeartUpperLimit" :options="{responsive: true, maintainAspectRatio: false}"></line-chart>
            
      <!-- <main-chart-example chartId="main-chart-01" class="chart-wrapper" style="height:300px;margin-top:40px;" height="300"></main-chart-example> -->
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
          <!-- <b-row> -->
             <button v-on:click="changeData">Change data</button>
            <!-- <b-table striped outlined stacked="sm" hover :items="tableItems" :fields="tableFields" head-variant="light">
           
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
            
          </b-table> -->
          <!-- <b-row>
            <b-col md="6" class="my-1">
              <b-pagination :total-rows="totalRows" :per-page="perPage" v-model="currentPage" class="my-0" />
            </b-col>
          </b-row> -->
          <!-- </b-row> -->
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
import LineChart from './dashboard/LineChart'
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
    LineChart,
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
      dataChartHeart: [],
      dataChartTemp: [],
      dataChartHeartLimit:[],
      dataChartHeartUpperLimit:[],
      dataChartTemperatureLimit:[],
      dataChartTemperatureUpperLimit:[],
      labelsData:[],
      statusDeviceInStr:"",
      statusDevice:"",
      conditions:"",
      test: [4, 4, 4, 4, 4, 4],
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
      startDate:"",
      endDate:"",
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
  // watch:{ 
  //   'selected_filter': function() {
  //     this.changeTime(this.selected_filter)  
  //   },
  //   'tanggalnya': function(){
  //     var temp = new Date(this.tanggalnya)
  //     this.tanggalnya_convert = temp
  //   } 
  // },
  created(){
      this.checkSession(); 
  },
  methods: {
    changeData: function() {
      // this.dataChart = [60, 6, 3, 5, 5, 6,6, 6, 3, 5, 5, 6];
      this.dataChartHeart.push(120);
      this.dataChartTemp.push(30);
      this.dataChartHeartLimit.push(20);
      this.dataChartHeartUpperLimit.push(40);
      this.dataChartTemperatureLimit.push(53);
      this.dataChartTemperatureUpperLimit.push(80);
      
      this.labelsData.push('nambah bulan');
      // this.labelsData = [
          
      //     "February",
      //     "March",
      //     "April",
      //     "May",
      //     "June",
      //     "July",
      //     "January"
      //   ]
    },
    filterData: function(){
      // var start_temp = new Date(this.startDate) 
      // var end_temp = new Date(this.endDate)
      // this.startDate = start_temp.toISOString()
      // this.endDate = end_temp.toISOString()
      console.log(this.startDate)
      this.processDataInTime()

    },
    changeTime: function(select_iterator) {
      if(select_iterator == 0){
        this.firstLoad();
      }else if(select_iterator==1){
        this.oneDay();
      }
      
    },
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
    async fetchDataToday(){
      const response = await PostsService.getDataToday(window.localStorage.getItem("token"),{
                          idSapi: this.$route.params.id
                        });
      return response.data;
    },
    async fetchDataInTime(){
      const response = await PostsService.getDataInTime(window.localStorage.getItem("token"),{
                          idSapi: this.$route.params.id,
                          start : this.startDate,
                          end: this.endDate
                        });
      return response.data;
    },
    soket(){
      this.socket.on('/topic/cows/detail/'+this.$route.params.id, (sapiData) => {
        this.nameOfCow = sapiData.namaSapi;
        this.tableItems = sapiData.perangkat.data;
        this.currentTemp = sapiData.perangkat.data[sapiData.perangkat.data.length-1].suhu.toFixed(2);
        this.currentHeart = sapiData.perangkat.data[sapiData.perangkat.data.length-1].jantung.toFixed(2);
        this.getBadge(sapiData.perangkat.status);
        this.getKondisi(sapiData.perangkat.data[sapiData.perangkat.data.length-1].kondisi);
        this.dateFormatter(sapiData.perangkat.data[sapiData.perangkat.data.length-1].tanggal);
        // Chart operation
        this.dataChartHeart.push(this.currentHeart);
        this.dataChartTemp.push(this.currentTemp);
        this.dataChartHeartLimit.push(20);
        this.dataChartHeartUpperLimit.push(40);
        this.dataChartTemperatureLimit.push(53);
        this.dataChartTemperatureUpperLimit.push(80);
        this.labelsData.push(this.dateOnFormat);
        //=======
        
      })
    },
    
    async firstLoad(){
      this.dataChartHeart= []
      this.dataChartTemp=[]
      this.dataChartHeartLimit=[]
      this.dataChartHeartUpperLimit=[]
      this.dataChartTemperatureLimit=[]
      this.dataChartTemperatureUpperLimit=[]
      this.labelsData=[]
      const response = await this.fetchDataToday();
      let sapiData = response.data[0]; //because response data in array
      // console.log(this.selected)
      this.nameOfCow = sapiData.namaSapi;
      this.tableItems = sapiData.perangkat.data;
      this.getBadge(sapiData.perangkat.status);
      this.getKondisi(sapiData.perangkat.data[sapiData.perangkat.data.length-1].kondisi);
      this.currentTemp = sapiData.perangkat.data[sapiData.perangkat.data.length-1].suhu.toFixed(2);
      this.currentHeart = sapiData.perangkat.data[sapiData.perangkat.data.length-1].jantung.toFixed(2);
      // for(var i=0;i<sapiData.perangkat.data.length;i++){
      //   this.dataChartHeart.push(sapiData.perangkat.data[i].suhu.toFixed(2));
      //   this.dataChartTemp.push(sapiData.perangkat.data[i].jantung.toFixed(2));
      //   this.dataChartHeartLimit.push(20);
      //   this.dataChartHeartUpperLimit.push(40);
      //   this.dataChartTemperatureLimit.push(53);
      //   this.dataChartTemperatureUpperLimit.push(80);
      //   this.dateFormatter(sapiData.perangkat.data[i].tanggal);
      //   this.labelsData.push(this.dateOnFormat);
      // }
      this.soket();
    },
    async processDataInTime(){
      this.dataChartHeart= []
      this.dataChartTemp=[]
      this.dataChartHeartLimit=[]
      this.dataChartHeartUpperLimit=[]
      this.dataChartTemperatureLimit=[]
      this.dataChartTemperatureUpperLimit=[]
       this.labelsData=[]
      const response = await this.fetchDataInTime();
      let sapiData = response.data[0]; //because response data in array
      // console.log(this.selected)
      this.nameOfCow = sapiData.namaSapi;
      this.tableItems = sapiData.perangkat.data;
      this.getBadge(sapiData.perangkat.status);
      this.getKondisi(sapiData.perangkat.data[sapiData.perangkat.data.length-1].kondisi);
      this.currentTemp = sapiData.perangkat.data[sapiData.perangkat.data.length-1].suhu.toFixed(2);
      this.currentHeart = sapiData.perangkat.data[sapiData.perangkat.data.length-1].jantung.toFixed(2);
      for(var i=0;i<sapiData.perangkat.data.length;i++){
        this.dataChartHeart.push(sapiData.perangkat.data[i].suhu.toFixed(2));
        this.dataChartTemp.push(sapiData.perangkat.data[i].jantung.toFixed(2));
        this.dataChartHeartLimit.push(20);
        this.dataChartHeartUpperLimit.push(40);
        this.dataChartTemperatureLimit.push(53);
        this.dataChartTemperatureUpperLimit.push(80);
        this.dateFormatter(sapiData.perangkat.data[i].tanggal);
        this.labelsData.push(this.dateOnFormat);
      }
    },
    async oneDay(){
      this.dataChartHeart= []
      this.dataChartTemp=[]
      this.dataChartHeartLimit=[]
      this.dataChartHeartUpperLimit=[]
      this.dataChartTemperatureLimit=[]
      this.dataChartTemperatureUpperLimit=[]
       this.labelsData=[]
      const response = await this.fetchDataToday();
      let sapiData = response.data[0]; //because response data in array
      // console.log(this.selected)
      this.nameOfCow = sapiData.namaSapi;
      this.tableItems = sapiData.perangkat.data;
      this.getBadge(sapiData.perangkat.status);
      this.getKondisi(sapiData.perangkat.data[sapiData.perangkat.data.length-1].kondisi);
      this.currentTemp = sapiData.perangkat.data[sapiData.perangkat.data.length-1].suhu.toFixed(2);
      this.currentHeart = sapiData.perangkat.data[sapiData.perangkat.data.length-1].jantung.toFixed(2);
      for(var i=0;i<sapiData.perangkat.data.length;i++){
        this.dataChartHeart.push(sapiData.perangkat.data[i].suhu.toFixed(2));
        this.dataChartTemp.push(sapiData.perangkat.data[i].jantung.toFixed(2));
        this.dataChartHeartLimit.push(20);
        this.dataChartHeartUpperLimit.push(40);
        this.dataChartTemperatureLimit.push(53);
        this.dataChartTemperatureUpperLimit.push(80);
        this.dateFormatter(sapiData.perangkat.data[i].tanggal);
        this.labelsData.push(this.dateOnFormat);
      }
    },
    getBadge (status) {
      if(status==0){
        this.statusDeviceInStr="Device Nonactive";
        this.statusDevice="danger"
      }else{
        this.statusDeviceInStr="Device Active";
        this.statusDevice="success"
      }
      return status == 0 ? 'danger' : 'success'
    },
    getKondisi(tmp){
      
      var kondisiPointer = 0;
      if(Number(tmp) == 0 ){
        this.CurrentConditions="Upnormal";
        this.conditions="danger"
      }else{
        kondisiPointer = 1;
        this.CurrentConditions="Normal";
        this.conditions="success"
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
