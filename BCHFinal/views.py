from django.shortcuts import render
import datetime

def games(request):
    context = {
        "game1":"""
        <h4>Dụng cụ & setup:</h4>
    <ul>
      <li>1 cây nến (thật)</li>
      <li>Đường thi dài 5m</li>
      <li>Dây chỉ (chạm sợi dây chỉ sẽ bị NPC quấy rối)</li>
      <li>Gió quạt, người hù nhẹ</li>
      <li>Đèn chớp</li>
      <li>Khu vực đích: bàn gỗ theo số thứ tự của từng đội</li>
    </ul>

    <h4>Cách chơi:</h4>
    <ul>
      <li>Mỗi đội chọn 1 người cầm nến (linh chủ)</li>
      <li>Khi hiệu lệnh "LỬA KHỞI", đội bắt đầu di chuyển</li>
      <li>Nếu nến tắt 2 lần thành viên đó sẽ phải thành người "trấn giữ cổng âm" (bị xuất hồn)</li>
      <li>Khi nến tắt lần thứ nhất phải đứng im tại chỗ để chờ NPC châm lửa mới</li>
      <li>Đội đến đích trước với nến còn cháy → chiến thắng chặng</li>
    </ul>

    <p><strong>Tính điểm:</strong> Tổng số nến còn cháy đến được đích của mỗi đội sẽ là tổng số điểm. 2đ/1 nến.</p>
    <p><strong>Lưu ý:</strong> Không được che chắn nến bằng áo hay tay quá sát.</p>
        """,
        "game2":"""<h4>Dụng cụ & setup:</h4>
    <ul>
      <li>1 khu vực dài 10–12m</li>
      <li>1 đèn pin nhỏ (cho người dẫn)</li>
      <li>1 khăn bịt mắt (cho người làm lễ)</li>
      <li>Loa nhỏ phát âm thanh "thì thầm, cười, kêu tên" để gây nhiễu</li>
    </ul>

    <h4>Cách chơi:</h4>
    <ul>
      <li>Mỗi đội chọn: 1 người làm lễ (bịt mắt), 1 người dẫn đường (cầm đèn pin, KHÔNG được nói)</li>
      <li>Các thành viên còn lại đứng ngoài hàng rào chỉ đạo bằng lời</li>
      <li>Người làm lễ đi theo tín hiệu tay của người dẫn (nghe chỉ đạo từ xa)</li>
      <li>BTC / đội khác có quyền gây nhiễu bằng cách gọi tên hoặc nói sai hướng</li>
      <li>Khi người làm lễ chạm tay vào vật "chuông / bát nhang" ở cuối đường → hoàn thành</li>
    </ul>

    <p><strong>Lưu ý:</strong> Không được dùng tay dẫn người bịt mắt.</p>""",
        "game3":"""<h4>Cách chơi:</h4>
    <ul>
      <li>Mỗi đội xếp hàng theo thứ tự 6–7 người</li>
      <li>BTC đọc câu chú 1 lần duy nhất cho người đầu tiên nghe</li>
      <li>Người đó nói mô tả lại cho người thứ hai</li>
      <li>Tiếp tục đến người cuối cùng</li>
      <li>Người cuối cùng đọc to câu nghe được</li>
      <li>BTC công bố sai lệch so với bản gốc</li>
    </ul>

    <p><strong>Lưu ý:</strong> Không được nói lớn hoặc viết ra. Có thể bật nhạc nền tiếng gió, chuông khi truyền để tăng độ nhiễu.</p>""",
        "game4":"""<h4>Dụng cụ:</h4>
    <ul>
      <li>1 tờ giấy A4 in phong cách cổ, có chữ và số in đỏ xen lẫn các dòng bình thường</li>
      <li>Puzzle ghép hình (sau bức hình có số điện thoại / dãy số để mở khóa lấy công cụ)</li>
    </ul>""",
        "game5":"""<p><strong>Setup:</strong> 1 em (áo trắng, tóc xõa), đứng quay lưng về phía người chơi, đồng hồ bấm giờ.</p>
    
    <h4>Cách chơi:</h4>
    <ul>
      <li>Tất cả đội đứng ở vạch xuất phát</li>
      <li>NPC quay lưng về phía họ</li>
      <li>Khi NPC bắt đầu đếm các số nguyên tố giảm dần, người chơi được phép di chuyển</li>
      <li>Khi NPC chuyển sang đếm các số nguyên tố tăng dần, NPC quay đầu lại – mọi người phải đứng yên tuyệt đối</li>
    </ul>

    <h4>Quy tắc phát hiện:</h4>
    <ul>
      <li>Khi NPC quay lại (đếm tăng), nếu thấy ai đang di chuyển / mất thăng bằng → người đó "bị nhập"</li>
      <li>"Bị nhập" = quay lại vạch xuất phát</li>
      <li>Nếu tái phạm 2 lần → loại khỏi vòng</li>
    </ul>

    <h4>Chiến thắng:</h4>
    <ul>
      <li>Đội chạm được vào vai NPC mà chưa bị phát hiện thì thắng vòng đó</li>
      <li>Nếu hết 3 lượt mà không ai chạm tới NPC, đội nào đứng gần nhất mà chưa bị nhập được xem là thắng</li>
    </ul>"""
    }
    today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7)))
    print(today.day, today.month, today.hour)
    if not (today.day == 9 and today.month == 11 and today.hour >= 14):
        context = {
            "game1": "<p style='color: yellow'><strong>~ Sẽ sớm thôi... các bí mật sẽ được bật mí!!</strong></p>",
            "game2": "<p style='color: yellow'><strong>~ Sẽ sớm thôi... các bí mật sẽ được bật mí!!</strong></p>",
            "game3": "<p style='color: yellow'><strong>~ Sẽ sớm thôi... các bí mật sẽ được bật mí!!</strong></p>",
            "game4": "<p style='color: yellow'><strong>~ Sẽ sớm thôi... các bí mật sẽ được bật mí!!</strong></p>",
            "game5": "<p style='color: yellow'><strong>~ Sẽ sớm thôi... các bí mật sẽ được bật mí!!</strong></p>",
        }
    return render(request, 'games.html', context)