//Page Object
Page({
    data: {
        name: "aming"
    },
    //options(Object)
    formSubmit: function (e) {
        console.log(e.detail.value.username)
        console.log(e.detail.value.password)
        console.log("he")
        wx.showModal({
            title: '标题',
            content: '内容',
            showCancel: true,
            cancelText: '取消',
            cancelColor: '#000000',
            confirmText: '确定',
            confirmColor: '#3CC51F',
            success: (result) => {
                if (result.confirm) {
                    console.log(result.confirm)
                    console.log('------------------')
                    wx.navigateTo({
                        url: 'index?id=333'
                    });
                      
                }
            },
            fail: () => { },
            complete: () => { }
        });

        wx.setNavigationBarTitle({
            title: '导航标题',
            success: (result) => {
                
            },
            fail: () => {},
            complete: () => {}
        });
          
    },
});