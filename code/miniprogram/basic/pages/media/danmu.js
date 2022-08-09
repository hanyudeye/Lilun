Page({
    onReady: function () {
        this.videoContext = wx.createVideoContext('myvideo', this);
        console.log(this.videoContext)
    },
    inputValue: "",
    inputblur(e) {
        this.inputValue = e.detail.value
    }, send() {
        this.videoContext.sendDanmu({
            text:this.inputValue,
            color:"#eee"
        })
    },play(){
        this.videoContext.play();
    },stop(){
        this.videoContext.pause();
    },jump(){
        this.videoContext.seek(5)
    }

})