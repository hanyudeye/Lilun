十分钟搞定Stable Diffusion！只需浏览器就能免費打造你的AI女神！(免显卡版) #StableDiffusion #ai绘图
- 第一步打开https://colab.research.google.com/
- 第二步打开GPU
- 第三步**安裝指令 **地址
https://pastebin.com/NqwteUJU


```
!pip install --upgrade fastapi==0.90.1
!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
!git clone https://github.com/yfszzx/stable-diffusion-webui-images-browser /content/stable-diffusion-webui/extensions/stable-diffusion-webui-images-browser
!curl -Lo chilloutmixni.safetensors https://huggingface.co/nolanaatama/chomni/resolve/main/chomni.safetensors
!curl -Lo ulzzang-6500.pt https://huggingface.co/nolanaatama/chomni/resolve/main/ulzzang-6500.pt
!mv "/content/chilloutmixni.safetensors" "/content/stable-diffusion-webui/models/Stable-diffusion"
!mv "/content/ulzzang-6500.pt" "/content/stable-diffusion-webui/embeddings"
%cd /content/stable-diffusion-webui
!COMMANDLINE_ARGS="--share --disable-safe-unpickle --skip-torch-cuda-test --no-half-vae --xformers --reinstall-xformers --enable-insecure-extension-access" REQS_FILE="requirements.txt" python launch.py
```

- 第四步：输入图片需求指令
(8k, RAW photo, best quality, masterpiece:1.2), (realistic, photo-realistic:1.37), ultra-detailed,full body,1 japanese girl, solo,beautiful detailed sky,detailed parkt,night,beautiful detailed eyes,beautiful detailed lips,professional lighting, photon mapping, radiosity, physically-based rendering,extremely detailed eyes and face, beautiful detailed eyes,light on face,cinematic lighting, white shirt, fishnet stockings, over a white shirt，uniform,1girl,full body,full-body shot,see-through,looking at viewer,outdoors,((black hair)),
第五步：输入图片不需要素材指令
EasyNegative, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans,extra fingers,fewer fingers,strange fingers,bad hand,signature, watermark, username, blurry, bad feet,bad leg, duplicate, extra limb, ugly, disgusting, poorly drawn hands, missing limb, floating limbs, disconnected limbs, malformed hands, blurry,mutated hands and fingers,, EasyNegative, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans,extra fingers,fewer fingers,strange fingers,bad hand,signature, watermark, username, blurry, bad feet,bad leg


