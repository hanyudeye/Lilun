Vue.component('account', {
    template: '<div><h2>账号模块</h2> <login></login></div>',
    components: {
        'login': {
            template: '<h3>登录模块</h3>'
        }
    }
});




var body = new Vue({
    el: '#app',
    data: {
        app: {
            title: '标题',
            time: '2020-10-30',
            showtime: true,
            colors: ['红', '绿', '蓝'],
        },
    },
    methods: {
        onmsg: function() {
            alert("你打我干嘛")
        },
    }


});
