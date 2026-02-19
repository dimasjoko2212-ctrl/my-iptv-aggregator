


# Script Generator Playlist M3U - FIXED VERSION
import os

channels = [
    # --- TV NASIONAL ---
    {"name": "TVRI Nasional", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/TVRI_Nasional_2019.svg/1200px-TVRI_Nasional_2019.svg.png", "group": "TV Nasional", "url": "https://ott-balancer.tvri.go.id/live/eds/Nasional/hls/Nasional.m3u8"},
    {"name": "Metro TV", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Metro_TV_2010.svg/1200px-Metro_TV_2010.svg.png", "group": "TV Berita", "url": "https://edge.medcom.id/live-edge/smil:metro.smil/playlist.m3u8"},
    {"name": "tvOne", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/TvOne_Logo_2011.svg/1200px-TvOne_Logo_2011.svg.png", "group": "TV Berita", "url": "http://202.80.222.20/cdn/iptv/Tvod/001/channel2000018/1024.m3u8|User-Agent=Mozilla/5.0"},
    
    # Trans Group & CNN butuh User-Agent agar bisa diputar di VLC/TiviMate
    {"name": "Trans TV", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Trans_TV_logo.svg/1200px-Trans_TV_logo.svg.png", "group": "TV Nasional", "url": "https://video.detik.com/transtv/smil:transtv.smil/playlist.m3u8|User-Agent=Mozilla/5.0"},
    {"name": "Trans 7", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/TRANS7.svg/1200px-TRANS7.svg.png", "group": "TV Nasional", "url": "https://video.detik.com/trans7/smil:trans7.smil/playlist.m3u8|User-Agent=Mozilla/5.0"},
    {"name": "CNN Indonesia", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/CNN_Indonesia.svg/1200px-CNN_Indonesia.svg.png", "group": "TV Berita", "url: "https://live.cnnindonesia.com/livecnn/smil:cnntv.smil/playlist.m3u8|User-Agent=Mozilla/5.0"},
    {"name": "CNBC Indonesia", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/CNBC_Indonesia.svg/1200px-CNBC_Indonesia.svg.png", "group": "TV Berita", "url": "https://live.cnbcindonesia.com/livecnbc/smil:cnbctv.smil/playlist.m3u8|User-Agent=Mozilla/5.0"},
    
    {"name": "Kompas TV", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Kompas_TV_logo_2017.svg/1200px-Kompas_TV_logo_2017.svg.png", "group": "TV Berita", "url": "https://op-group1-swiftservehd-1.dens.tv/h/h234/index.m3u|User-Agent=Mozilla/5.08"},
    {"name": "RRI NET", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/RRI_NET.svg/1200px-RRI_NET.svg.png", "group": "Radio Visual", "url": "https://private-streaming.rri.go.id/memfs/6f77c7b5-feb2-4935-9f89-e7e9fca0a54a_output_0.m3u8"},

    # --- RADIO AUDIO ---
    {"name": "RRI Pro 1 FM 90.9", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/RRI_Pro_1.svg/1200px-RRI_Pro_1.svg.png", "group": "Radio", "url": "ISI_URL_STREAMING_DARI_SNIFFER"},
    {"name": "RRI Pro 2 FM 92.5", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/RRI_Pro_2.svg/1200px-RRI_Pro_2.svg.png", "group": "Radio", "url": "ISI_URL_STREAMING_DARI_SNIFFER"},
    {"name": "RRI Pro 3 - KBRN - FM 88.8", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/RRI_Pro_3.svg/1200px-RRI_Pro_3.svg.png", "group": "Radio", "url": "https://stream-node0.rri.co.id/streaming/14/9014/kbrn.mp3"},
    {"name": "RRI Pro 4 FM 88.5", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/RRI_Pro_4.svg/1200px-RRI_Pro_4.svg.png", "group": "Radio", "url": "ISI_URL_STREAMING_DARI_SNIFFER"},
    {"name": "Elshinta", "logo": "https://elshinta.com/images/logo.png?v=1", "group": "Radio", "url": "https://stream-ssl.arenastreaming.com:8000/jakarta"},
]

def generate_m3u():
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for ch in channels:
            # Generate format M3U standard
            f.write(f'#EXTINF:-1 tvg-logo="{ch["logo"]}" group-title="{ch["group"]}", {ch["name"]}\n')
            f.write(f'{ch["url"]}\n')
    print("Mantap! File playlist.m3u berhasil dibuat.")

if __name__ == "__main__":
    generate_m3u()
