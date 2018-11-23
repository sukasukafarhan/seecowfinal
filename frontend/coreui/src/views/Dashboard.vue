<template>
  <div class="animated fadeIn">
    <b-row>
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
        <b-card header="Cow List">
          <b-row>
             <b-col sm="12" lg="12">
              <b-row>
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
                        <callout-chart-example chartId="callout-chart-01" v-bind:data="TemperatureGraph" variant="info" width="80" height="30" />
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
                        <callout-chart-example chartId="callout-chart-02" :data="[0, 59, 84, 84, 51, 55, 40]" variant="danger" width="80" height="30" />
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
            <b-table striped outlined stacked="sm" hover :items="tableItems" :fields="tableFields" head-variant="light">
            <div slot="namaSapi" slot-scope="data">
              <img src="img/cow/cow (2).png" width="50px" alt="CoreUI Logo">
              <strong>{{data.value}}</strong>
            </div>
            <div slot="key-kondisi" slot-scope="data">
              <b-badge :variant="getKondisi(data.item.perangkat.data[data.item.perangkat.data.length-1].suhu,data.item.perangkat.data[data.item.perangkat.data.length-1].jantung)">{{CurrentConditions}}</b-badge>
            </div>
            <div slot="key-tanggal" slot-scope="data">
              
              <strong>{{data.item.perangkat.data[data.item.perangkat.data.length-1].tanggal}}</strong>
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
          </b-table>
          </b-row>
          
        </b-card>
      </b-col>
    </b-row>
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
                <div class="progress-group mb-5">
                  <div class="progress-group-header">
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
import PostsService from "@/services/PostsService";

export default {
  name: 'dashboard',
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
      title: [],
      DeviceActive:0,
      DeviceNonActive:0,
      TemperatureAverage:0,
      HeartRateAverage:0,
      TemperatureGraph:[0, 23, 56, 22, 97,100,100],
      CurrentConditions:"",
      suhuArrange:[],
      statusDeviceInStr:"",
      sapiList:[],
      selected: 'Month',
      tableItems: [],
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
        }
      ]
    }
  },
  created(){
      // setInterval(function () {
      //   this.getds();
      // }.bind(this), 60000);
      setInterval(function () { 
        this.getds();
      }.bind(this), 25000); 
  },
  methods: {
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
    async getPosts() {
      const response = await PostsService.fetchPosts();
      this.title.push(response.data);
    },
    countArrange: function(datas){
      var rata=0;
      // for (var i=0;i<datas.length;i++){
      //   rata+=datas.perangkat.data[datas.perangkat.data.length-1].suhu
      // }
      // rata = rata/datas.length
      console.log(datas)
    },
    async fetchDataSapi(){
      const response = await PostsService.getSapi();
      return response.data;
    },
    async getds(){
      const response = await this.fetchDataSapi();
      let sapiData = response.sapi;
      var active =0,inActive =0,avgSuhu=0,avgHeart=0;
      for(var i=0;i<sapiData.length;i++){
        avgSuhu += Number(sapiData[i].perangkat.data[sapiData[i].perangkat.data.length-1].suhu);
        avgHeart += Number(sapiData[i].perangkat.data[sapiData[i].perangkat.data.length-1].jantung);
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
      console.log(this.tableItems);
    },
    getBadge (status) {
      if(status==0){
        this.statusDeviceInStr="Nonactive";
      }else{
        this.statusDeviceInStr="Active";
      }
      return status == 0 ? 'danger' : 'success'
    },
    getKondisi(tmp,hr){
      
      var kondisiPointer = 0;
      if(Number(tmp) < 20 || Number(tmp) > 40 || Number(hr) < 53 || Number(hr) > 80){
        this.CurrentConditions="Tidak Normal";
      }else{
        kondisiPointer = 1;
        this.CurrentConditions="Normal";
      }
      return kondisiPointer == 0 ? 'danger' : 'success'
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
