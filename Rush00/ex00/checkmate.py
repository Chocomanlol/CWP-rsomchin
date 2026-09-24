def checkmate(board):
    #เช็คว่าเป็น str มั้ยถ้าไม่ใช้ str ให้เลิกทำ
    if not board or not isinstance(board, str):
        return
    
    # แยก str เพื่อดูว่ามีคำมั้ย
    lines = []
    for line in board.splitlines(): 
        if line:
            lines.append(line) 
            
    if not lines:
        return

    #ขนาดของ list
    size = len(lines)
    
    #เช็คว่ากระดานเป็นสี่เหลี่ยมจัตุรัสหรือไม่
    for line in lines:
        if len(line) != size:
            return
        
    #ค้นหาตำแหน่งของ King ('K') ======================================
    king_r = -1
    king_c = -1 
    king_count = 0

    #หาตำแหน่งของ K บนกระดาน
    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                king_r = r
                king_c = c
                king_count += 1
                
    #ถ้า K ไม่เท่ากับ 1 ให้เลิกทำ
    if king_count != 1: 
        return
    
    #รายชื่อตัวหมากรุก
    chess_pieces = {'K', 'R', 'Q', 'B', 'P'}

    #ตำแหน่งเริ่มต้นของการเช็คแบบ บนล่าง-ซ้ายขวา ==============================
    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_directions:
        r = king_r + dr 
        c = king_c + dc
        while 0 <= r < size and 0 <= c < size: #เช็คต่อไปเรื่อยๆหาก rc ยังอยู่ในกระดาน
            piece = lines[r][c] 
            if piece in chess_pieces: 
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                break
            # ขยับพิกัดไปยังช่องถัดไปตามทิศทางเดิม
            r += dr
            c += dc

    #ตำแหน่งเริ่มต้นของการเช็คแบบเฉียง =======================================
    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_directions:
        r = king_r + dr
        c = king_c + dc 
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece in chess_pieces:
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    #เช็กการรุกจากเบี้ย =====================================================
    pawn_directions = [(1, -1), (1, 1)]
    for dr, dc in pawn_directions:
        pr = king_r + dr
        pc = king_c + dc
        if 0 <= pr < size and 0 <= pc < size:
            if lines[pr][pc] == 'P':
                print("Success")
                return

    print("Fail")