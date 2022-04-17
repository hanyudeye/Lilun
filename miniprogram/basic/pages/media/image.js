Page({
    data: {
        imageurl: ""
    }, viewPic() {

        wx.chooseImage({
            count: 9,
            sizeType: ['original', 'compressed'],
            sourceType: ['album', 'camera'],
            success: (result) => {
                console.log(result)

                wx.getImageInfo({
                    src: result.tempFilePaths[0],
                    success: (result)=>{
                       console.log(result) 
                    },
               });

           },
        });

    },onLoad(){
    }

})