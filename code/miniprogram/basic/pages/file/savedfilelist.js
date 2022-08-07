Page({
show(){
    wx.getSavedFileList({
        success: (result)=>{
            console.log(result)
        },
        fail: ()=>{},
        complete: ()=>{}
    });
},openfile(){
wx.openDocument({
    filePath: "http://tmp/11.docx",
    fileType: 'docx',
    success: (result)=>{
       console.log(result) 
    },
});
}
})