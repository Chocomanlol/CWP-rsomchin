def checkmate(board):
    # 1. ตรวจสอบความถูกต้องเบื้องต้นของข้อความ
    if not board or not isinstance(board, str): #บอร์ดเป็น str มั้ย ถ้าไม่ใช่ ให้ false 
        return

    # แยกกระดานออกเป็นบรรทัดๆ
    lines = [] # list ชื่อ line 
    for line in board.splitlines(): #split แยก String ด้วยการขึ้นบรรทัดใหม่
        if line:
            lines.append(line) #ถ้ามีข้อมูลให้เพิ่มเข้า line

    if not lines: #ถ้าแยกบรรทัดแล้วไม่พบข้อมูลเลย ให้หยุดการทำงาน
        return

    size = len(lines) #len บอกจำนวนตัวใน list

    # ตรวจว่ากระดานเป็นสี่เหลี่ยมจัตุรัสหรือไม่
    for line in lines: #วนใน list
        if len(line) != size: #ขนาดไม่เท่ากันให้หยุดทำงาน
            return

    # 2. ค้นหาตำแหน่งของ King ('K')
    king_r = -1 #row
    king_c = -1 #column
    king_count = 0 #จำนวนที่พบ

    for r in range(size): #ลูป 2 รอบเช็คทุกตัวอักษรบนกระดาน row
        for c in range(size): #column
            if lines[r][c] == 'K': #ถ้าเจอ K
                king_r = r #บันทึก row
                king_c = c #บันทึก column
                king_count += 1 #เพิ่มจำนวน K

    # ถ้า K มากกว่า 1 หรือไม่เจอ เลิกทำ
    if king_count != 1:
        return

    # 3. เช็กแนวตรง (ขึ้น, ลง, ซ้าย, ขวา) -> หา Rook ('R') หรือ Queen ('Q')
    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_directions: #วนลูปตรวจทีละทิศทางจากทั้งหมด 4 ทิศทาง
        # คำนวณพิกัดช่องถัดไปโดยขยับออกจาก King ไป 1 ช่องตามทิศทางนั้น
        r = king_r + dr 
        c = king_c + dc
        # วนลูปขยับเดินหน้าไปเรื่อยๆ ตราบใดที่พิกัด (r, c) ยังอยู่ในขอบเขตกระดาน
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c] # อ่านค่าตัวหมากในช่องปัจจุบัน
            if piece != '.': # ถ้าพบตัวหมาก (ไม่ใช่ช่องว่าง '.')
                if piece == 'R' or piece == 'Q': # ถ้าตัวหมากนั้นเป็น R หรือ Q แสดงว่า King ถูกรุกแนวตรง!
                    print("Success")# พิมพ์ Success และจบฟังก์ชันทันที
                    return 
                break  # หากเป็นตัวหมากชนิดอื่นจะบังสายตาขวางทางไว้ ทำให้ไม่โดนรุกจากทิศนี้ห้หยุดสแกนทิศนี้ทันที แล้วไปตรวจทิศถัดไป
            r += dr # ขยับพิกัดไปยังช่องถัดไปตามทิศทางเดิม
            c += dc

    # 4. เช็กแนวเฉียง (4 ทิศ) -> หา Bishop ('B') หรือ Queen ('Q')
    # กำหนดเวกเตอร์ทิศทางแนวเฉียง:
    # (-1, -1) = บนซ้าย | (-1, 1) = บนขวา | (1, -1) = ล่างซ้าย | (1, 1) = ล่างขวา
    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # วนลูปตรวจทีละทิศทางเฉียง
    for dr, dc in diagonal_directions:
        r = king_r + dr
        c = king_c + dc
        # วนลูปขยับเดินหน้าในแนวเฉียงไปเรื่อยๆ ตราบใดที่ยังไม่ตกขอบกระดาน
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece != '.':
                if piece == 'B' or piece == 'Q':
                    print("Success")
                    return
                break  # เจอตัวอื่นขวางทาง ให้หยุดดูทิศนี้
            r += dr
            c += dc

    # 5. เช็ก Pawn ('P')
    # Pawn กินขึ้นข้างบน ดังนั้น Pawn ที่รุก King ได้ ต้องอยู่เฉียงล่างของ King 1 ช่องพอดี
    pawn_positions = [(king_r + 1, king_c - 1), (king_r + 1, king_c + 1)]
    for pr, pc in pawn_positions:
        if 0 <= pr < size and 0 <= pc < size:
            if lines[pr][pc] == 'P':
                print("Success")
                return

    # ถ้าตรวจสอบครบทุกทิศแล้วไม่โดนรุก
    print("Fail")