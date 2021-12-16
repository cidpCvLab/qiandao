var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

var data = 1;

function present_data(time_data) {
    option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                // Use axis to trigger tooltip
                type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
            }
        },
        legend: {},
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value'
        },
        yAxis: {
            type: 'category',
            data: time_data.member
        },
        series: [{
                name: "Mon",
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: time_data.Mon
            },
            {
                name: "Tues",
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: time_data.Tues
            },
            {
                name: "Wed",
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: time_data.Wed
            },
            {
                name: "Thur",
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: time_data.Thur
            },
            {
                name: "Fri",
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: time_data.Fri
            },
            {
                name: "Sat",
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: time_data.Sat
            },
            {
                name: "Sun",
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: time_data.Sun
            }
        ]
    };
    var myChart = echarts.init(chartDom);
    option && myChart.setOption(option);
    myChart.setOption(option);
};

async function request_data() {
    var response = await axios.get('http://192.168.1.223:522/data', {params: {begin_time: 1636329600, end_time: 1636934400, member: 20}});
    present_data(response.data)
};

request_data();