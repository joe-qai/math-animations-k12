# 渲染全部课时视频（1080p / 30fps），并复制到站点 assets/videos/
# 用法：powershell -ExecutionPolicy Bypass -File video_build/render_all.ps1

$ErrorActionPreference = "Continue"
$env:PYTHONIOENCODING = "utf-8"
Set-Location $PSScriptRoot

New-Item -ItemType Directory -Force -Path "logs" | Out-Null
New-Item -ItemType Directory -Force -Path "..\assets\videos" | Out-Null

$jobs = @(
    @{ File = "scene_coushi.py";      Scene = "CoushiScene";      Id = "coushifa" },
    @{ File = "scene_renshi.py";      Scene = "RenshiScene";      Id = "renshi-tuxing" },
    @{ File = "scene_fenlei.py";      Scene = "FenleiScene";      Id = "fenlei-zhengli" },
    @{ File = "scene_zhongbiao.py";   Scene = "ZhongbiaoScene";   Id = "renshi-zhongbiao" },
    @{ File = "scene_hunhe.py";       Scene = "HunheScene";       Id = "lianjia-lianjian" },
    @{ File = "scene_jiao.py";        Scene = "JiaoScene";        Id = "jiao-renshi" },
    @{ File = "scene_tiaoxing.py";    Scene = "TiaoxingScene";    Id = "tiaoxing-tongji" },
    @{ File = "scene_celiang.py";     Scene = "CeliangScene";     Id = "celiang-shifenmiao" },
    @{ File = "scene_duowei.py";      Scene = "DuoweiScene";      Id = "duowei-cheng-yiwei" },
    @{ File = "scene_chufa_yiwei.py"; Scene = "ChufaYiweiScene"; Id = "chufa-yiwei" },
    @{ File = "scene_changfangxing_mianji.py"; Scene = "ChangfangxingMianjiScene"; Id = "changfangxing-mianji" },
    @{ File = "scene_fenshu.py";      Scene = "FenshuChubuScene"; Id = "fenshu-chubu" },
    @{ File = "scene_xiaoshu.py";     Scene = "XiaoshuChubuScene"; Id = "xiaoshu-chubu" },
    @{ File = "scene_pingyi.py";      Scene = "PingyiScene";      Id = "pingyi-xuanzhuan" },
    @{ File = "scene_dashu.py";       Scene = "DashuJianfaScene"; Id = "dashu-jianfa" },
    @{ File = "scene_xian.py";        Scene = "XianYuJiaoScene"; Id = "xian-yujiao" },
    @{ File = "scene_yunsuan.py";     Scene = "YunSuanLvScene";  Id = "yun-suanlv" },
    @{ File = "scene_xiaoshu_cheng.py"; Scene = "XiaoshuChengScene"; Id = "xiaoshu-cheng" },
    @{ File = "scene_pingxing.py";    Scene = "PingxingSibianxingScene"; Id = "pingxing-sibianxing" },
    @{ File = "scene_chengfa.py";     Scene = "ChengfaScene";     Id = "chengfa-yiyi" },
    @{ File = "scene_chufa.py";       Scene = "ChufaScene";       Id = "chufa-yiyi" },
    @{ File = "scene_sanjiaoxing.py"; Scene = "SanjiaoxingScene"; Id = "sanjiaoxing-mianji" },
    @{ File = "scene_fangcheng.py";   Scene = "FangchengScene";   Id = "yiyuan-yici-fangcheng" },
    @{ File = "scene_wanquan.py";     Scene = "WanquanScene";     Id = "wanquan-pingfang" },
    @{ File = "scene_dengcha.py";     Scene = "DengchaScene";     Id = "dengcha-shulie" }
)

foreach ($j in $jobs) {
    Write-Output ("[RENDER] " + $j.Id)
    manim -qh --fps 30 $j.File $j.Scene 2>&1 | Out-File ("logs\" + $j.Scene + ".log") -Encoding utf8

    $stem = [System.IO.Path]::GetFileNameWithoutExtension($j.File)
    $src = Join-Path "media\videos\$stem\1080p30" ($j.Scene + ".mp4")
    if (Test-Path $src) {
        Copy-Item $src ("..\assets\videos\" + $j.Id + ".mp4") -Force
        $size = [math]::Round((Get-Item $src).Length / 1MB, 2)
        Write-Output ("[OK] " + $j.Id + "  " + $size + " MB")
    } else {
        Write-Output ("[FAIL] " + $j.Id + "  missing: " + $src)
    }
}

Write-Output "[ALL DONE]"