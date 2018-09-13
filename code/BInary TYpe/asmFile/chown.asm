;
; +-------------------------------------------------------------------------+
; |   This file	has been generated by The Interactive Disassembler (IDA)    |
; |	      Copyright	(c) 2015 Hex-Rays, <support@hex-rays.com>	    |
; |			 License info: 48-B611-7234-BB			    |
; |		Doskey Lee, Kingsoft Internet Security Software		    |
; +-------------------------------------------------------------------------+
;
; Input	MD5   :	EA2C232D45E2BCA2DFD0C521C226D6CB
; Input	CRC32 :	716DBBEC

; File Name   :	D:\coreutils-o\chown.o
; Format      :	ELF for	Intel 386 (Relocatable)
;
; Source File :	'chown.c'

		.686p
		.mmx
		.model flat
.intel_syntax noprefix

; ===========================================================================

; Segment type:	Pure code
; Segment permissions: Read/Execute
_text		segment	byte public 'CODE' use32
		assume cs:_text
		;org 8000000h
		assume es:nothing, ss:nothing, ds:_text, fs:nothing, gs:nothing

; =============== S U B	R O U T	I N E =======================================

; Attributes: static bp-based frame

; void emit_ancillary_info()
emit_ancillary_info proc near		; CODE XREF: usage+1D2p

lc_messages	= dword	ptr -0Ch
var_4		= dword	ptr -4

		push	ebp
		mov	ebp, esp
		push	ebx
		sub	esp, 14h
		mov	eax, ds:program_name
		sub	esp, 0Ch
		push	eax
		call	last_component
		add	esp, 10h
		mov	ebx, eax
		sub	esp, 0Ch
		push	offset msgid	; "\nReport %s bugs to %s\n"
		call	gettext
		add	esp, 10h
		sub	esp, 4
		push	offset aBugCoreutils@g ; "bug-coreutils@gnu.org"
		push	ebx
		push	eax		; format
		call	printf
		add	esp, 10h
		sub	esp, 0Ch
		push	offset aSHomePageHttpW ; "%s home page:	<http://www.gnu.org/softw"...
		call	gettext
		add	esp, 10h
		sub	esp, 4
		push	offset domainname ; "coreutils"
		push	offset aGnuCoreutils ; "GNU coreutils"
		push	eax		; format
		call	printf
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aGeneralHelpUsi ; "General help using GNU software: <http:"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		sub	esp, 8
		push	0		; locale
		push	5		; category
		call	setlocale
		add	esp, 10h
		mov	[ebp+lc_messages], eax
		cmp	[ebp+lc_messages], 0
		jz	short loc_80000E6
		sub	esp, 4
		push	3		; n
		push	offset s2	; "en_"
		push	[ebp+lc_messages] ; s1
		call	strncmp
		add	esp, 10h
		test	eax, eax
		jz	short loc_80000E6
		mov	eax, ds:program_name
		sub	esp, 0Ch
		push	eax
		call	last_component
		add	esp, 10h
		mov	ebx, eax
		sub	esp, 0Ch
		push	offset aReportSTransla ; "Report %s translation	bugs to	<http://t"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax		; format
		call	printf
		add	esp, 10h

loc_80000E6:				; CODE XREF: emit_ancillary_info+9Bj
					; emit_ancillary_info+B4j
		mov	eax, ds:program_name
		sub	esp, 0Ch
		push	eax
		call	last_component
		add	esp, 10h
		mov	ebx, eax
		sub	esp, 0Ch
		push	offset aForCompleteDoc ; "For complete documentation, run: info	c"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax		; format
		call	printf
		add	esp, 10h
		nop
		mov	ebx, [ebp+var_4]
		leave
		retn
emit_ancillary_info endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: static bp-based frame

; char *__cdecl	bad_cast(const char *s)
bad_cast	proc near		; CODE XREF: main+54Cp

s		= dword	ptr  8

		push	ebp
		mov	ebp, esp
		mov	eax, [ebp+s]
		pop	ebp
		retn
bad_cast	endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: noreturn bp-based	frame

; void __cdecl usage(int status)
		public usage
usage		proc near		; CODE XREF: main+28Fp	main+2D1p ...

status		= dword	ptr  8

		push	ebp
		mov	ebp, esp
		push	edi
		push	esi
		push	ebx
		sub	esp, 0Ch
		cmp	[ebp+status], 0
		jz	short loc_8000163
		mov	ebx, ds:program_name
		sub	esp, 0Ch
		push	offset aTrySHelpForMor ; "Try `%s --help' for more information.\n"
		call	gettext
		add	esp, 10h
		mov	edx, eax
		mov	eax, ds:stderr
		sub	esp, 4
		push	ebx
		push	edx		; format
		push	eax		; stream
		call	fprintf
		add	esp, 10h
		jmp	loc_80002FB
; ---------------------------------------------------------------------------

loc_8000163:				; CODE XREF: usage+Dj
		mov	esi, ds:program_name
		mov	ebx, ds:program_name
		sub	esp, 0Ch
		push	offset aUsageSOption__ ; "Usage: %s [OPTION]...	[OWNER][:[GROUP]]"...
		call	gettext
		add	esp, 10h
		sub	esp, 4
		push	esi
		push	ebx
		push	eax		; format
		call	printf
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aChangeTheOwner ; "Change the owner and/or group	of each	F"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aHNoDereference ; "  -h,	--no-dereference   affect each sy"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aFromCurrent_ow ; "	--from=CURRENT_OWNER:CURRENT_GROU"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aNoPreserveRoot ; "	--no-preserve-root  do not treat "...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aFSilentQuietSu ; "  -f,	--silent, --quiet  suppress most "...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aTheFollowingOp ; "The following	options	modify how a hier"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aHelpDisplayThi ; "	--help	   display this	help and "...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aVersionOutputV ; "	--version  output version informa"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	ebx, ds:stdout
		sub	esp, 0Ch
		push	offset aOwnerIsUnchang ; "\nOwner is unchanged if missing.  Group"...
		call	gettext
		add	esp, 10h
		sub	esp, 8
		push	ebx
		push	eax
		call	fputs_unlocked
		add	esp, 10h
		mov	edi, ds:program_name
		mov	esi, ds:program_name
		mov	ebx, ds:program_name
		sub	esp, 0Ch
		push	offset aExamplesSRootU ; "\nExamples:\n	 %s root /u	   Change"...
		call	gettext
		add	esp, 10h
		push	edi
		push	esi
		push	ebx
		push	eax		; format
		call	printf
		add	esp, 10h
		call	emit_ancillary_info

loc_80002FB:				; CODE XREF: usage+3Aj
		sub	esp, 0Ch
		push	[ebp+status]	; status
		call	exit
usage		endp


; =============== S U B	R O U T	I N E =======================================

; Attributes: noreturn bp-based	frame

; int __cdecl main(int argc, const char	**argv,	const char **envp)
		public main
main		proc near

argv		= dword	ptr -0CCh
preserve_root	= byte ptr -0BEh
ok		= byte ptr -0BDh
uid		= dword	ptr -0BCh
gid		= dword	ptr -0B8h
required_uid	= dword	ptr -0B4h
required_gid	= dword	ptr -0B0h
u_dummy		= dword	ptr -0ACh
bit_flags	= dword	ptr -0A8h
dereference	= dword	ptr -0A4h
optc		= dword	ptr -0A0h
e		= dword	ptr -9Ch
e_0		= dword	ptr -98h
chopt		= Chown_option ptr -94h
ref_stats	= stat ptr -7Ch
var_1C		= dword	ptr -1Ch
argc		= dword	ptr  0Ch
envp		= dword	ptr  14h

		lea	ecx, [esp+4]
		and	esp, 0FFFFFFF0h
		push	dword ptr [ecx-4]
		push	ebp
		mov	ebp, esp
		push	edi
		push	esi
		push	ebx
		push	ecx
		sub	esp, 0C8h
		mov	ebx, ecx
		mov	eax, [ebx+4]
		mov	[ebp+argv], eax
		mov	eax, large gs:14h
		mov	[ebp+var_1C], eax
		xor	eax, eax
		mov	[ebp+preserve_root], 0
		mov	[ebp+uid], 0FFFFFFFFh
		mov	[ebp+gid], 0FFFFFFFFh
		mov	[ebp+required_uid], 0FFFFFFFFh
		mov	[ebp+required_gid], 0FFFFFFFFh
		mov	[ebp+bit_flags], 10h
		mov	[ebp+dereference], 0FFFFFFFFh
		mov	eax, [ebp+argv]
		mov	eax, [eax]
		sub	esp, 0Ch
		push	eax
		call	set_program_name
		add	esp, 10h
		sub	esp, 8
		push	offset s	; locale
		push	6		; category
		call	setlocale
		add	esp, 10h
		sub	esp, 8
		push	offset dirname	; "/usr/local/share/locale"
		push	offset domainname ; "coreutils"
		call	bindtextdomain
		add	esp, 10h
		sub	esp, 0Ch
		push	offset domainname ; "coreutils"
		call	textdomain
		add	esp, 10h
		sub	esp, 0Ch
		push	offset close_stdout ; func
		call	atexit
		add	esp, 10h
		sub	esp, 0Ch
		lea	eax, [ebp+chopt]
		push	eax
		call	chopt_init
		add	esp, 10h
		jmp	loc_80005DC
; ---------------------------------------------------------------------------

loc_80003E8:				; CODE XREF: main+302j
		mov	eax, [ebp+optc]
		cmp	eax, 66h
		jz	loc_800057B
		cmp	eax, 66h
		jg	short loc_8000446
		cmp	eax, 4Ch
		jz	loc_800049B
		cmp	eax, 4Ch
		jg	short loc_800042A
		cmp	eax, 0FFFFFF7Eh
		jz	loc_8000590
		cmp	eax, 48h
		jz	short loc_800048C
		cmp	eax, 0FFFFFF7Dh
		jz	loc_800059A
		jmp	loc_80005D2
; ---------------------------------------------------------------------------

loc_800042A:				; CODE XREF: main+102j
		cmp	eax, 52h
		jz	loc_8000566
		cmp	eax, 63h
		jz	loc_800056F
		cmp	eax, 50h
		jz	short loc_80004AA
		jmp	loc_80005D2
; ---------------------------------------------------------------------------

loc_8000446:				; CODE XREF: main+F4j
		cmp	eax, 81h
		jz	loc_80004FE
		cmp	eax, 81h
		jg	short loc_8000472
		cmp	eax, 76h
		jz	loc_8000584
		cmp	eax, 80h
		jz	short loc_80004C8
		cmp	eax, 68h
		jz	short loc_80004B9
		jmp	loc_80005D2
; ---------------------------------------------------------------------------

loc_8000472:				; CODE XREF: main+150j
		cmp	eax, 83h
		jz	short loc_80004E3
		cmp	eax, 83h
		jl	short loc_80004D7
		cmp	eax, 84h
		jz	short loc_80004EF
		jmp	loc_80005D2
; ---------------------------------------------------------------------------

loc_800048C:				; CODE XREF: main+112j
		mov	[ebp+bit_flags], 11h
		jmp	loc_80005DC
; ---------------------------------------------------------------------------

loc_800049B:				; CODE XREF: main+F9j
		mov	[ebp+bit_flags], 2
		jmp	loc_80005DC
; ---------------------------------------------------------------------------

loc_80004AA:				; CODE XREF: main+139j
		mov	[ebp+bit_flags], 10h
		jmp	loc_80005DC
; ---------------------------------------------------------------------------

loc_80004B9:				; CODE XREF: main+165j
		mov	[ebp+dereference], 0
		jmp	loc_80005DC
; ---------------------------------------------------------------------------

loc_80004C8:				; CODE XREF: main+160j
		mov	[ebp+dereference], 1
		jmp	loc_80005DC
; ---------------------------------------------------------------------------

loc_80004D7:				; CODE XREF: main+178j
		mov	[ebp+preserve_root], 0
		jmp	loc_80005DC
; ---------------------------------------------------------------------------

loc_80004E3:				; CODE XREF: main+171j
		mov	[ebp+preserve_root], 1
		jmp	loc_80005DC
; ---------------------------------------------------------------------------

loc_80004EF:				; CODE XREF: main+17Fj
		mov	eax, ds:optarg
		mov	ds:reference_file, eax
		jmp	loc_80005DC
; ---------------------------------------------------------------------------

loc_80004FE:				; CODE XREF: main+145j
		mov	eax, ds:optarg
		sub	esp, 0Ch
		lea	edx, [ebp+ref_stats]
		push	edx
		lea	edx, [ebp+u_dummy]
		push	edx
		lea	edx, [ebp+required_gid]
		push	edx
		lea	edx, [ebp+required_uid]
		push	edx
		push	eax
		call	parse_user_spec
		add	esp, 20h
		mov	[ebp+e], eax
		cmp	[ebp+e], 0
		jz	short loc_8000563
		mov	eax, ds:optarg
		sub	esp, 0Ch
		push	eax
		call	quote
		add	esp, 10h
		sub	esp, 0Ch
		push	eax
		push	[ebp+e]
		push	offset format	; "%s: %s"
		push	0		; errnum
		push	1		; status
		call	error
		add	esp, 20h

loc_8000563:				; CODE XREF: main+22Fj
		nop
		jmp	short loc_80005DC
; ---------------------------------------------------------------------------

loc_8000566:				; CODE XREF: main+127j
		mov	[ebp+chopt.recurse], 1
		jmp	short loc_80005DC
; ---------------------------------------------------------------------------

loc_800056F:				; CODE XREF: main+130j
		mov	[ebp+chopt.verbosity], 1
		jmp	short loc_80005DC
; ---------------------------------------------------------------------------

loc_800057B:				; CODE XREF: main+EBj
		mov	[ebp+chopt.force_silent], 1
		jmp	short loc_80005DC
; ---------------------------------------------------------------------------

loc_8000584:				; CODE XREF: main+155j
		mov	[ebp+chopt.verbosity], 0
		jmp	short loc_80005DC
; ---------------------------------------------------------------------------

loc_8000590:				; CODE XREF: main+109j
		sub	esp, 0Ch
		push	0		; status
		call	usage
; ---------------------------------------------------------------------------

loc_800059A:				; CODE XREF: main+119j
		mov	edx, ds:Version
		mov	eax, ds:stdout
		sub	esp, 4
		push	0
		push	offset aJimMeyering ; "Jim Meyering"
		push	offset aDavidMackenzie ; "David	MacKenzie"
		push	edx
		push	offset aGnuCoreutils ; "GNU coreutils"
		push	offset aChown	; "chown"
		push	eax
		call	version_etc
		add	esp, 20h
		sub	esp, 0Ch
		push	0		; status
		call	exit
; ---------------------------------------------------------------------------

loc_80005D2:				; CODE XREF: main+11Fj	main+13Bj ...
		sub	esp, 0Ch
		push	1		; status
		call	usage
; ---------------------------------------------------------------------------

loc_80005DC:				; CODE XREF: main+DDj main+190j ...
		sub	esp, 0Ch
		push	0		; longind
		push	offset long_options ; longopts
		push	offset shortopts ; "HLPRcfhv"
		push	[ebp+argv]	; argv
		push	dword ptr [ebx]	; argc
		call	getopt_long
		add	esp, 20h
		mov	[ebp+optc], eax
		cmp	[ebp+optc], 0FFFFFFFFh
		jnz	loc_80003E8
		movzx	eax, [ebp+chopt.recurse]
		test	al, al
		jz	short loc_8000657
		cmp	[ebp+bit_flags], 10h
		jnz	short loc_8000661
		cmp	[ebp+dereference], 1
		jnz	short loc_800064B
		sub	esp, 0Ch
		push	offset aRDereferenceRe ; "-R --dereference requires either -H or "...
		call	gettext
		add	esp, 10h
		sub	esp, 4
		push	eax		; format
		push	0		; errnum
		push	1		; status
		call	error
		add	esp, 10h

loc_800064B:				; CODE XREF: main+323j
		mov	[ebp+dereference], 0
		jmp	short loc_8000661
; ---------------------------------------------------------------------------

loc_8000657:				; CODE XREF: main+311j
		mov	[ebp+bit_flags], 10h

loc_8000661:				; CODE XREF: main+31Aj	main+34Fj
		cmp	[ebp+dereference], 0
		setnz	al
		mov	[ebp+chopt.affect_symlink_referent], al
		mov	eax, ds:optind
		mov	edx, [ebx]
		sub	edx, eax
		mov	eax, ds:reference_file
		test	eax, eax
		jz	short loc_800068A
		mov	eax, 1
		jmp	short loc_800068F
; ---------------------------------------------------------------------------

loc_800068A:				; CODE XREF: main+37Bj
		mov	eax, 2

loc_800068F:				; CODE XREF: main+382j
		cmp	edx, eax
		jge	short loc_800070C
		mov	eax, ds:optind
		cmp	[ebx], eax
		jg	short loc_80006BE
		sub	esp, 0Ch
		push	offset aMissingOperand ; "missing operand"
		call	gettext
		add	esp, 10h
		sub	esp, 4
		push	eax		; format
		push	0		; errnum
		push	0		; status
		call	error
		add	esp, 10h
		jmp	short loc_8000702
; ---------------------------------------------------------------------------

loc_80006BE:				; CODE XREF: main+394j
		mov	eax, [ebx]
		add	eax, 3FFFFFFFh
		lea	edx, ds:0[eax*4]
		mov	eax, [ebp+argv]
		add	eax, edx
		mov	eax, [eax]
		sub	esp, 0Ch
		push	eax
		call	quote
		add	esp, 10h
		mov	ebx, eax
		sub	esp, 0Ch
		push	offset aMissingOpera_0 ; "missing operand after	%s"
		call	gettext
		add	esp, 10h
		push	ebx
		push	eax		; format
		push	0		; errnum
		push	0		; status
		call	error
		add	esp, 10h

loc_8000702:				; CODE XREF: main+3B6j
		sub	esp, 0Ch
		push	1		; status
		call	usage
; ---------------------------------------------------------------------------

loc_800070C:				; CODE XREF: main+38Bj
		mov	eax, ds:reference_file
		test	eax, eax
		jz	loc_80007A9
		mov	eax, ds:reference_file
		sub	esp, 8
		lea	edx, [ebp+ref_stats]
		push	edx
		push	eax
		call	stat64
		add	esp, 10h
		test	eax, eax
		jz	short loc_800076B
		mov	eax, ds:reference_file
		sub	esp, 0Ch
		push	eax
		call	quote
		add	esp, 10h
		mov	esi, eax
		sub	esp, 0Ch
		push	offset aFailedToGetAtt ; "failed to get	attributes of %s"
		call	gettext
		add	esp, 10h
		mov	ebx, eax
		call	__errno_location
		mov	eax, [eax]
		push	esi
		push	ebx		; format
		push	eax		; errnum
		push	1		; status
		call	error
		add	esp, 10h

loc_800076B:				; CODE XREF: main+42Aj
		mov	eax, [ebp+ref_stats.st_uid]
		mov	[ebp+uid], eax
		mov	eax, [ebp+ref_stats.st_gid]
		mov	[ebp+gid], eax
		mov	eax, [ebp+ref_stats.st_uid]
		sub	esp, 0Ch
		push	eax
		call	uid_to_name
		add	esp, 10h
		mov	[ebp+chopt.user_name], eax
		mov	eax, [ebp+ref_stats.st_gid]
		sub	esp, 0Ch
		push	eax
		call	gid_to_name
		add	esp, 10h
		mov	[ebp+chopt.group_name],	eax
		jmp	loc_800086D
; ---------------------------------------------------------------------------

loc_80007A9:				; CODE XREF: main+40Dj
		mov	eax, ds:optind
		lea	edx, ds:0[eax*4]
		mov	eax, [ebp+argv]
		add	eax, edx
		mov	eax, [eax]
		sub	esp, 0Ch
		lea	edx, [ebp+chopt]
		add	edx, 14h
		push	edx
		lea	edx, [ebp+chopt]
		add	edx, 10h
		push	edx
		lea	edx, [ebp+gid]
		push	edx
		lea	edx, [ebp+uid]
		push	edx
		push	eax
		call	parse_user_spec
		add	esp, 20h
		mov	[ebp+e_0], eax
		cmp	[ebp+e_0], 0
		jz	short loc_8000839
		mov	eax, ds:optind
		lea	edx, ds:0[eax*4]
		mov	eax, [ebp+argv]
		add	eax, edx
		mov	eax, [eax]
		sub	esp, 0Ch
		push	eax
		call	quote
		add	esp, 10h
		sub	esp, 0Ch
		push	eax
		push	[ebp+e_0]
		push	offset format	; "%s: %s"
		push	0		; errnum
		push	1		; status
		call	error
		add	esp, 20h

loc_8000839:				; CODE XREF: main+4F4j
		mov	eax, [ebp+chopt.user_name]
		test	eax, eax
		jnz	short loc_8000860
		mov	eax, [ebp+chopt.group_name]
		test	eax, eax
		jz	short loc_8000860
		sub	esp, 0Ch
		push	offset s	; s
		call	bad_cast
		add	esp, 10h
		mov	[ebp+chopt.user_name], eax

loc_8000860:				; CODE XREF: main+53Bj	main+542j
		mov	eax, ds:optind
		add	eax, 1
		mov	ds:optind, eax

loc_800086D:				; CODE XREF: main+49Ej
		movzx	eax, [ebp+chopt.recurse]
		test	al, al
		jz	short loc_80008D9
		cmp	[ebp+preserve_root], 0
		jz	short loc_80008D9
		sub	esp, 0Ch
		push	offset dev_ino_buf_5258
		call	get_root_dev_ino
		add	esp, 10h
		mov	[ebp+chopt.root_dev_ino], eax
		mov	eax, [ebp+chopt.root_dev_ino]
		test	eax, eax
		jnz	short loc_80008D9
		sub	esp, 0Ch
		push	offset asc_80016A7 ; "/"
		call	quote
		add	esp, 10h
		mov	esi, eax
		sub	esp, 0Ch
		push	offset aFailedToGetAtt ; "failed to get	attributes of %s"
		call	gettext
		add	esp, 10h
		mov	ebx, eax
		call	__errno_location
		mov	eax, [eax]
		push	esi
		push	ebx		; format
		push	eax		; errnum
		push	1		; status
		call	error
		add	esp, 10h

loc_80008D9:				; CODE XREF: main+570j	main+579j ...
		or	[ebp+bit_flags], 400h
		mov	ebx, [ebp+required_gid]
		mov	ecx, [ebp+required_uid]
		mov	edx, [ebp+gid]
		mov	eax, [ebp+uid]
		mov	esi, ds:optind
		lea	edi, ds:0[esi*4]
		mov	esi, [ebp+argv]
		add	edi, esi
		sub	esp, 4
		lea	esi, [ebp+chopt]
		push	esi
		push	ebx
		push	ecx
		push	edx
		push	eax
		push	[ebp+bit_flags]
		push	edi
		call	chown_files
		add	esp, 20h
		mov	[ebp+ok], al
		sub	esp, 0Ch
		lea	eax, [ebp+chopt]
		push	eax
		call	chopt_free
		add	esp, 10h
		cmp	[ebp+ok], 0
		jz	short loc_8000955
		mov	eax, 0
		jmp	short loc_800095A
; ---------------------------------------------------------------------------

loc_8000955:				; CODE XREF: main+646j
		mov	eax, 1

loc_800095A:				; CODE XREF: main+64Dj
		sub	esp, 0Ch
		push	eax		; status

loc_800095E:				; DATA XREF: .eh_frame:080016CCo
					; .eh_frame:080016F0o ...
		call	exit
main		endp

_text		ends

; ===========================================================================

; Segment type:	Zero-length
; Segment permissions: Read/Write
_data		segment	byte public 'DATA' use32
_data		ends

; ===========================================================================

; Segment type:	Uninitialized
; Segment permissions: Read/Write
_bss		segment	dword public 'BSS' use32
		assume cs:_bss
		;org 8000964h
		assume es:nothing, ss:nothing, ds:_text, fs:nothing, gs:nothing
; char *reference_file
reference_file	dd ?			; DATA XREF: main+1EEw	main+374r ...
; Function-local static	variable
; dev_ino dev_ino_buf_5258
dev_ino_buf_5258 dev_ino <?>		; DATA XREF: main+57Eo
_bss		ends

; ===========================================================================

; Segment type:	Pure data
; Segment permissions: Read
; Segment alignment '32byte' can not be represented in assembly
_rodata		segment	para public 'CONST' use32
		assume cs:_rodata
		;org 8000980h
; char msgid[]
msgid		db 0Ah			; DATA XREF: emit_ancillary_info+1Do
		db 'Report %s bugs to %s',0Ah,0
aBugCoreutils@g	db 'bug-coreutils@gnu.org',0 ; DATA XREF: emit_ancillary_info+2Do
		align 10h
; char aSHomePageHttpW[]
aSHomePageHttpW	db '%s home page: <http://www.gnu.org/software/%s/>',0Ah,0
					; DATA XREF: emit_ancillary_info+3Fo
; char domainname[]
domainname	db 'coreutils',0        ; DATA XREF: emit_ancillary_info+4Fo
					; main+9Eo ...
aGnuCoreutils	db 'GNU coreutils',0    ; DATA XREF: emit_ancillary_info+54o
					; main+2AFo
		align 4
; char aGeneralHelpUsi[]
aGeneralHelpUsi	db 'General help using GNU software: <http://www.gnu.org/gethelp/>',0Ah,0
					; DATA XREF: emit_ancillary_info+6Bo
; char s2[]
s2		db 'en_',0              ; DATA XREF: emit_ancillary_info+A2o
; char aReportSTransla[]
aReportSTransla	db 'Report %s translation bugs to <http://translationproject.org/team'
					; DATA XREF: emit_ancillary_info+CCo
		db '/>',0Ah,0
		align 4
; char aForCompleteDoc[]
aForCompleteDoc	db 'For complete documentation, run: info coreutils ',27h,'%s invocation'
					; DATA XREF: emit_ancillary_info+FCo
		db 27h,0Ah,0
aRecursive	db 'recursive',0        ; DATA XREF: .rodata:long_optionso
aChanges	db 'changes',0          ; DATA XREF: .rodata:long_optionso
aDereference	db 'dereference',0      ; DATA XREF: .rodata:long_optionso
aFrom		db 'from',0             ; DATA XREF: .rodata:long_optionso
aNoDereference	db 'no-dereference',0   ; DATA XREF: .rodata:long_optionso
aNoPreserveRo_0	db 'no-preserve-root',0 ; DATA XREF: .rodata:long_optionso
aPreserveRoot	db 'preserve-root',0    ; DATA XREF: .rodata:long_optionso
aQuiet		db 'quiet',0            ; DATA XREF: .rodata:long_optionso
aSilent		db 'silent',0           ; DATA XREF: .rodata:long_optionso
aReference	db 'reference',0        ; DATA XREF: .rodata:long_optionso
aVerbose	db 'verbose',0          ; DATA XREF: .rodata:long_optionso
aHelp		db 'help',0             ; DATA XREF: .rodata:long_optionso
aVersion	db 'version',0          ; DATA XREF: .rodata:long_optionso
		align 20h
; const	option long_options[14]
long_options	option <offset aRecursive, 0, 0, 52h> ;	DATA XREF: main+2DBo
		option <offset aChanges, 0, 0, 63h> ; "recursive"
		option <offset aDereference, 0,	0, 80h>
		option <offset aFrom, 1, 0, 81h>
		option <offset aNoDereference, 0, 0, 68h>
		option <offset aNoPreserveRo_0,	0, 0, 82h>
		option <offset aPreserveRoot, 0, 0, 83h>
		option <offset aQuiet, 0, 0, 66h>
		option <offset aSilent,	0, 0, 66h>
		option <offset aReference, 1, 0, 84h>
		option <offset aVerbose, 0, 0, 76h>
		option <offset aHelp, 0, 0, 0FFFFFF7Eh>
		option <offset aVersion, 0, 0, 0FFFFFF7Dh>
		option	<0>
; char aTrySHelpForMor[]
aTrySHelpForMor	db 'Try `%s --help',27h,' for more information.',0Ah,0
					; DATA XREF: usage+18o
		align 4
; char aUsageSOption__[]
aUsageSOption__	db 'Usage: %s [OPTION]... [OWNER][:[GROUP]] FILE...',0Ah
					; DATA XREF: usage+4Eo
		db '  or:  %s [OPTION]... --reference=RFILE FILE...',0Ah,0
		align 4
; char aChangeTheOwner[]
aChangeTheOwner	db 'Change the owner and/or group of each FILE to OWNER and/or GROUP.'
					; DATA XREF: usage+72o
		db 0Ah
		db 'With --reference, change the owner and group of each FILE to thos'
		db 'e of RFILE.',0Ah
		db 0Ah
		db '  -c, --changes          like verbose but report only when a chan'
		db 'ge is made',0Ah
		db '      --dereference      affect the referent of each symbolic lin'
		db 'k (this is',0Ah
		db '                         the default), rather than the symbolic l'
		db 'ink itself',0Ah,0
		align 4
; char aHNoDereference[]
aHNoDereference	db '  -h, --no-dereference   affect each symbolic link instead of any'
					; DATA XREF: usage+95o
		db ' referenced',0Ah
		db '                         file (useful only on systems that can ch'
		db 'ange the',0Ah
		db '                         ownership of a symlink)',0Ah,0
		align 10h
; char aFromCurrent_ow[]
aFromCurrent_ow	db '      --from=CURRENT_OWNER:CURRENT_GROUP',0Ah ; DATA XREF: usage+B8o
		db '                         change the owner and/or group of each fi'
		db 'le only if',0Ah
		db '                         its current owner and/or group match tho'
		db 'se specified',0Ah
		db '                         here.  Either may be omitted, in which c'
		db 'ase a match',0Ah
		db '                         is not required for the omitted attribut'
		db 'e.',0Ah,0
		align 4
; char aNoPreserveRoot[]
aNoPreserveRoot	db '      --no-preserve-root  do not treat `/',27h,' specially (the defa'
					; DATA XREF: usage+DBo
		db 'ult)',0Ah
		db '      --preserve-root    fail to operate recursively on `/',27h,0Ah,0
; char aFSilentQuietSu[]
aFSilentQuietSu	db '  -f, --silent, --quiet  suppress most error messages',0Ah
					; DATA XREF: usage+FEo
		db '      --reference=RFILE  use RFILE',27h,'s owner and group rather th'
		db 'an',0Ah
		db '                         specifying OWNER:GROUP values',0Ah
		db '  -R, --recursive        operate on files and directories recursi'
		db 'vely',0Ah
		db '  -v, --verbose          output a diagnostic for every file proce'
		db 'ssed',0Ah
		db 0Ah,0
; char aTheFollowingOp[]
aTheFollowingOp	db 'The following options modify how a hierarchy is traversed when th'
					; DATA XREF: usage+121o
		db 'e -R',0Ah
		db 'option is also specified.  If more than one is specified, only th'
		db 'e final',0Ah
		db 'one takes effect.',0Ah
		db 0Ah
		db '  -H                     if a command line argument is a symbolic'
		db ' link',0Ah
		db '                         to a directory, traverse it',0Ah
		db '  -L                     traverse every symbolic link to a direct'
		db 'ory',0Ah
		db '                         encountered',0Ah
		db '  -P                     do not traverse any symbolic links (defa'
		db 'ult)',0Ah
		db 0Ah,0
; char aHelpDisplayThi[]
aHelpDisplayThi	db '      --help     display this help and exit',0Ah,0
					; DATA XREF: usage+144o
		align 4
; char aVersionOutputV[]
aVersionOutputV	db '      --version  output version information and exit',0Ah,0
					; DATA XREF: usage+167o
		align 4
; char aOwnerIsUnchang[]
aOwnerIsUnchang	db 0Ah			; DATA XREF: usage+18Ao
		db 'Owner is unchanged if missing.  Group is unchanged if missing, bu'
		db 't changed',0Ah
		db 'to login group if implied by a `:',27h,' following a symbolic OWNER.'
		db 0Ah
		db 'OWNER and GROUP may be numeric as well as symbolic.',0Ah,0
; char aExamplesSRootU[]
aExamplesSRootU	db 0Ah			; DATA XREF: usage+1B9o
		db 'Examples:',0Ah
		db '  %s root /u        Change the owner of /u to "root".',0Ah
		db '  %s root:staff /u  Likewise, but also change its group to "staff'
		db '".',0Ah
		db '  %s -hR root /u    Change the owner of /u and subfiles to "root"'
		db '.',0Ah,0
; char s
s		db 0			; DATA XREF: main+87o main+547o
; char dirname[]
dirname		db '/usr/local/share/locale',0 ; DATA XREF: main+99o
; char format[]
format		db '%s: %s',0           ; DATA XREF: main+24Co main+522o
aJimMeyering	db 'Jim Meyering',0     ; DATA XREF: main+2A4o
aDavidMackenzie	db 'David MacKenzie',0  ; DATA XREF: main+2A9o
aChown		db 'chown',0            ; DATA XREF: main+2B4o
; char shortopts[]
shortopts	db 'HLPRcfhv',0         ; DATA XREF: main+2E0o
		align 4
; char aRDereferenceRe[]
aRDereferenceRe	db '-R --dereference requires either -H or -L',0 ; DATA XREF: main+328o
; char aMissingOperand[]
aMissingOperand	db 'missing operand',0  ; DATA XREF: main+399o
; char aMissingOpera_0[]
aMissingOpera_0	db 'missing operand after %s',0 ; DATA XREF: main+3E1o
		align 4
; char aFailedToGetAtt[]
aFailedToGetAtt	db 'failed to get attributes of %s',0 ; DATA XREF: main+442o
					; main+5B0o
asc_80016A7	db '/',0                ; DATA XREF: main+59Eo
_rodata		ends

; ===========================================================================

; Segment type:	Pure data
; Segment permissions: Read
_eh_frame	segment	dword public 'CONST' use32
		assume cs:_eh_frame
		;org 80016ACh
		dd 14h,	0
		dd 527A01h, 1087C01h, 4040C1Bh,	188h, 20h, 1Ch
		dd offset loc_800095E-800202Ah
		dd 11Ch, 80E4100h, 0D420285h, 3834405h,	0C5011403h, 4040CC3h
		dd 1Ch,	40h
		dd offset loc_800095E-8001F32h
		dd 8, 80E4100h,	0D420285h, 0CC54405h, 404h, 1Ch, 60h
		dd offset loc_800095E-8001F4Ah
		dd 1E2h, 80E4100h, 0D420285h, 3874605h,	5830486h, 2Ch
		dd 80h
		dd offset loc_800095E-8001D88h
		dd 65Dh, 10C4400h, 5104700h, 46007502h,	7075030Fh, 2071006h
		dd 6107C75h, 10787502h,	74750203h
_eh_frame	ends

; ===========================================================================

; Segment type:	Externs
; extern
		extrn program_name:dword ; DATA	XREF: emit_ancillary_info+7r
					; emit_ancillary_info+B6r ...
		extrn last_component:near ; CODE XREF: emit_ancillary_info+10p
					; emit_ancillary_info+BFp ...
; char *gettext(const char *msgid)
		extrn gettext:near	; CODE XREF: emit_ancillary_info+22p
					; emit_ancillary_info+44p ...
; int printf(const char	*format, ...)
		extrn printf:near	; CODE XREF: emit_ancillary_info+34p
					; emit_ancillary_info+5Ap ...
; struct _IO_FILE *stdout
		extrn stdout:dword	; DATA XREF: emit_ancillary_info+62r
					; usage+69r ...
		extrn fputs_unlocked:near ; CODE XREF: emit_ancillary_info+7Dp
					; usage+84p ...
; char *setlocale(int category,	const char *locale)
		extrn setlocale:near	; CODE XREF: emit_ancillary_info+8Cp
					; main+8Ep
; int strncmp(const char *s1, const char *s2, size_t n)
		extrn strncmp:near	; CODE XREF: emit_ancillary_info+AAp
; struct _IO_FILE *stderr
		extrn stderr:dword	; DATA XREF: usage+27r
; int fprintf(FILE *stream, const char *format,	...)
		extrn fprintf:near	; CODE XREF: usage+32p
; void exit(int	status)
		extrn exit:near		; CODE XREF: usage+1DDp main+2C7p ...
		extrn set_program_name:near ; CODE XREF: main+7Cp
; char *bindtextdomain(const char *domainname, const char *dirname)
		extrn bindtextdomain:near ; CODE XREF: main+A3p
; char *textdomain(const char *domainname)
		extrn textdomain:near	; CODE XREF: main+B3p
; void close_stdout(void)
		extrn close_stdout	; DATA XREF: main+BEo
; int atexit(void (*func)(void))
		extrn atexit:near	; CODE XREF: main+C3p
		extrn chopt_init:near	; CODE XREF: main+D5p
; char *optarg
		extrn optarg:dword	; DATA XREF: main:loc_80004EFr
					; main:loc_80004FEr ...
		extrn parse_user_spec:near ; CODE XREF:	main+21Ap main+4DFp
		extrn quote:near	; CODE XREF: main+23Ap	main+3D4p ...
; void error(int status, int errnum, const char	*format, ...)
		extrn error:near	; CODE XREF: main+255p	main+33Dp ...
		extrn Version:dword	; DATA XREF: main:loc_800059Ar
		extrn version_etc:near	; CODE XREF: main+2BAp
; int getopt_long(int argc, char *const	*argv, const char *shortopts, const struct option *longopts, int *longind)
		extrn getopt_long:near	; CODE XREF: main+2EDp
; int optind
		extrn optind:dword	; DATA XREF: main+36Br	main+38Dr ...
		extrn stat64:near	; CODE XREF: main+420p
; int *_errno_location(void)
		extrn __errno_location:near ; CODE XREF: main+451p main+5BFp
		extrn uid_to_name:near	; CODE XREF: main+47Ep
		extrn gid_to_name:near	; CODE XREF: main+493p
		extrn get_root_dev_ino:near ; CODE XREF: main+583p
		extrn chown_files:near	; CODE XREF: main+61Fp
		extrn chopt_free:near	; CODE XREF: main+637p


		end