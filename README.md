# WebRTC Video Call

Demo video call 1-1 giữa hai trình duyệt. Python server chỉ làm signaling:
chuyển tiếp SDP offer/answer và ICE candidate; media đi trực tiếp giữa hai
peer qua WebRTC.

## Tính năng

- Gọi video và audio real-time giữa hai tab/trình duyệt.
- Signaling qua Flask-SocketIO.
- Trao đổi SDP và ICE candidate.
- Giao diện HTML/CSS đơn giản để kiểm tra cuộc gọi.

## Kiến trúc

Mỗi trình duyệt lấy camera/microphone và tạo `RTCPeerConnection`. Flask-SocketIO
giới hạn demo ở hai peer và relay các message signaling giữa chúng. Sau khi
thương lượng xong, luồng audio/video không đi qua server signaling.

## Chạy nhanh

```bash
git clone https://github.com/haibadguy/webrtc-video-call.git
cd webrtc-video-call
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
python server.py
```

Mở `http://localhost:5000` trong hai tab. Cho phép camera/microphone, sau đó
bấm **Start call** ở một tab. Khi deploy, server dùng port từ biến môi trường
`PORT` nếu nền tảng cung cấp.

## Công nghệ

Python, Flask, Flask-SocketIO, Eventlet, WebRTC, SDP, ICE, JavaScript,
HTML/CSS.

## Giới hạn

- Demo chỉ hỗ trợ tối đa hai peer trong một process.
- Chưa có xác thực, phòng riêng hoặc lưu trữ người dùng.
- STUN mặc định phù hợp cho demo; NAT traversal production cần TURN.
- Camera/microphone thường yêu cầu localhost hoặc HTTPS.

## License

MIT
