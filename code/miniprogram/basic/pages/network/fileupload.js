const app = getApp();
const serviceurl = app.globalData.serviceurl;
// pages/network/fileupload.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },
  uploadfile() {
    wx.chooseImage({
      count: 9,
      sizeType: ['original', 'compressed'],
      sourceType: ['album', 'camera'],
      success: (result) => {
        var tempFilePath = result.tempFilePaths;

        // console.log(tempFilePath);
        //上传多个文件
        tempFilePath.forEach(element => {

          wx.uploadFile({
            url: serviceurl + '/api/file/uploadImage',
            filePath: element,
            name: 'image',
            success: (result) => {
              // console.log(result)
              if (result.statusCode == 200) {
                // console.log(result.data)
               let res = JSON.parse(result.data);
                console.log(res.path);
              }
            }
          });

        });


      },
    });


  },

})