Page({
    data:
    {
        userInfo: []
    },
    handleUserinfo(res) {
        // console.log(res)
        if (res.detail.userInfo) {
            this.setData({
                userInfo: res.detail.userInfo
            });
        }
    },
    onLoad() {
        const that = this
        // console.log(this)
        wx.getUserInfo({
            success: function (res) {
                // console.log(res)
                that.setData({
                    userInfo: res.userInfo
                });
            }
        });
    }
})