Page({
    data: {
        filepath: ''

    },
    record() {
        wx.startRecord({
            success: (result) => {
                console.log(result.tempFilePath)

                //长久保存
                wx.saveFile({
                    tempFilePath: result.tempFilePath,
                    success: (result) => {
                        console.log(result.savedFilePath)

                        this.setData({
                            filepath: result.savedFilePath
                        });
                    },
                });


            },
        });

        setTimeout(function () {
            //结束录音，设置10秒后停止
            wx.stopRecord();
        }, 10000)
    }, stoprecord() {
        //手动结束录音
        wx.stopRecord();
    },playvoice(){
        let path=this.data.filepath;

        // console.log(this.data)
        // console.log('----')

        wx.playVoice({
            filePath: path,
            duration: 60,
            success: (result)=>{
               console.log("eh") 
            },
        });
    }

})