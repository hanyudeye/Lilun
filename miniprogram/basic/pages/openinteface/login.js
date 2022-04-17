Page({
    login() {
        wx.login({
            timeout: 10000,
            success: (result) => {
                console.log(result)
            },
        });
    },onShareAppMessage(){
        return {
            title:"登录分享",
            desc:"快来登录",
            path:"/pages/basic/icon"
        }
    }
})