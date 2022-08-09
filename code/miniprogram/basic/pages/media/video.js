Page({
    data: {
        src: ''
    }, getvideo() {

        wx.chooseVideo({
            sourceType: ['album', 'camera'],
            compressed: true,
            maxDuration: 15,
            success: (result) => {
                this.setData({
                    src: result.tempFilePath
                })
            },
        });
    }
})