    page    ,132
    title   memset - set sections of memory all to one byte
;***
;memset.asm - set a section of memory to all one byte
;
;   Copyright (c) Microsoft Corporation. All rights reserved.
;
;Purpose:
;   contains the memset() routine
;
;*******************************************************************************

    .xlist
    include cruntime.inc
    .list

page
;***
;char *memset(dst, value, count) - sets "count" bytes at "dst" to "value"
;
;Purpose:
;   Sets the first "count" bytes of the memory starting
;   at "dst" to the character value "value".
;
;   Algorithm:
;   char *
;   memset (dst, value, count)
;       char *dst;
;       char value;
;       unsigned int count;
;       {
;       char *start = dst;
;
;       while (count--)
;           *dst++ = value;
;       return(start);
;       }
;
;Entry:
;   char *dst - pointer to memory to fill with value
;   char value - value to put in dst bytes
;   int count - number of bytes of dst to fill
;
;Exit:
;   returns dst, with filled bytes
;
;Uses:
;
;Exceptions:
;
;*******************************************************************************

    CODESEG

    extrn   _VEC_memset:near
    extrn   __isa_available:dword
    extrn   __isa_enabled:dword
    extrn   __favor:dword

    public  memset
memset proc \
        dst:ptr byte, \
        value:byte, \
        count:dword

        OPTION PROLOGUE:NONE, EPILOGUE:NONE

    .FPO    ( 0, 3, 0, 0, 0, 0 )

    mov edx,[esp + 0ch] ; edx = "count"
    mov ecx,[esp + 4]   ; ecx points to "dst"

    test    edx,edx     ; 0?
    jz      toend   ; if so, nothing to do


    movzx   eax, BYTE PTR [esp + 8] ; the byte "value" to be stored

; See if Enhanced Fast Strings makes sense.
    ; ENFSTRG supported?
    bt      __favor, __FAVOR_ENFSTRG
    jnc     SSE2CheckA                 ; no jump
    ; use Enhanced Fast Strings
    mov     ecx,[esp + 0ch] ; get the count
    push    edi
    mov     edi, [esp+8]   ;get dst
    rep     stosb
    jmp short finish         ; Done
SSE2CheckA:
    mov edx,[esp + 0ch] ; restore the count
SSE2CheckB:
; Special case large block zeroing using SSE2 support
    cmp     edx,080h    ; block size exceeds size threshold?
    jl      dword_align ; no, go use dword
    bt      __isa_enabled, __ISA_AVAILABLE_SSE2
    jc      _VEC_memset ; yes, use xmm large block set
; Align address on dword boundary
dword_align:

    push    edi     ; preserve edi
    mov edi,ecx     ; edi = dest pointer

    cmp edx,4       ; if it's less then 4 bytes
    jb  tail        ; tail needs edi and edx to be initialized

    neg ecx
    and ecx,3       ; ecx = # bytes before dword boundary
    jz  short dwords    ; jump if address already aligned

    sub edx,ecx     ; edx = adjusted count (for later)
adjust_loop:
    mov [edi],al
    add edi,1
    sub ecx,1
    jnz adjust_loop

dwords:
; set all 4 bytes of eax to [value]
    mov ecx,eax     ; ecx=0/0/0/value
    shl eax,8       ; eax=0/0/value/0

    add eax,ecx     ; eax=0/0val/val

    mov ecx,eax     ; ecx=0/0/val/val

    shl eax,10h     ; eax=val/val/0/0

    add eax,ecx     ; eax = all 4 bytes = [value]

; Set dword-sized blocks
    mov ecx,edx     ; move original count to ecx
    and edx,3       ; prepare in edx byte count (for tail loop)
    shr ecx,2       ; adjust ecx to be dword count
    jz  tail        ; jump if it was less then 4 bytes

    rep stosd
main_loop_tail:
    test    edx,edx     ; if there is no tail bytes,
    jz  finish      ; we finish, and it's time to leave
; Set remaining bytes

tail:
    mov [edi],al    ; set remaining bytes
    add edi,1

    sub edx,1       ; if there is some more bytes
    jnz tail        ; continue to fill them

; Done
finish:
    mov eax,[esp + 8]   ; return dest pointer
    pop edi     ; restore edi

    ret

toend:
    mov eax,[esp + 4]   ; return dest pointer

    ret

memset  endp

    end
