#!/bin/bash

export HOMEH=/home/nguyen.tran-van/yocto-rcar_v5/ext-src
export ATF_HOME=$HOMEH/arm-trusted-firmware
export MBEDTLS_DIR=$HOMEH/mbedtls

unset LD_LIBRARY_PATH
unset PKG_CONFIG_PATH
source /home/nguyen.tran-van/sdk/environment-setup-aarch64-poky-linux

# get from branch name
cd $ATF_HOME
BRANCH=`git branch | grep "\*" | awk '{print $2}' | sed 's./._.g'`
STORE_TARGET=build_${BRANCH}

ATFW_OPT_LOSSY="RCAR_LOSSY_ENABLE=1"
# ATFW_OPT_LOSSY=""
ATFW_OPT_ulcb=" RCAR_GEN3_ULCB=1 PMIC_LEVEL_MODE=0"
PLATFORM="rcar"

# FROM YOCTO RECIPE ###########################################
# COMPATIBLE_MACHINE = "(salvator-x|ulcb|ebisu)"
# PLATFORM = "rcar"
# ATFW_OPT_LOSSY = "${@oe.utils.conditional("USE_MULTIMEDIA", "1", "RCAR_LOSSY_ENABLE=1", "", d)}"
# ATFW_OPT_r8a7795 = "LSI=H3 RCAR_DRAM_SPLIT=1 RCAR_DRAM_LPDDR4_MEMCONF=0 ${ATFW_OPT_LOSSY}"
# ATFW_OPT_r8a7796 = "LSI=M3 RCAR_DRAM_SPLIT=2 ${ATFW_OPT_LOSSY}"
# ATFW_OPT_r8a77965 = "LSI=M3N ${ATFW_OPT_LOSSY}"
# ATFW_OPT_r8a77990 = "LSI=E3 RCAR_SA0_SIZE=0 RCAR_AVS_SETTING_ENABLE=0 RCAR_DRAM_DDR3L_MEMCONF=0 RCAR_DRAM_DDR3L_MEMDUAL=0"
# ATFW_OPT_append_ulcb = " RCAR_GEN3_ULCB=1 PMIC_LEVEL_MODE=0"

# IPL build options for H3/E3/H3ULCB
# EXTRA_ATFW_OPT ?= ""
# EXTRA_ATFW_CONF ?= ""

# H3ULCB[4x2g] = "LSI=H3 RCAR_DRAM_SPLIT=1 RCAR_GEN3_ULCB=1 PMIC_LEVEL_MODE=0"
# H3[2x2g] = "LSI=H3 RCAR_DRAM_SPLIT=2 RCAR_DRAM_CHANNEL=5"
# H3[4x2g] = "LSI=H3 RCAR_DRAM_SPLIT=1"
# E3[4d] = "LSI=E3 RCAR_SA0_SIZE=0 RCAR_AVS_SETTING_ENABLE=0 RCAR_DRAM_DDR3L_MEMCONF=1 RCAR_DRAM_DDR3L_MEMDUAL=1"

# oe_runmake bl2 bl31 rcar_layout_tool rcar_srecord PLAT=${PLATFORM} SPD=opteed MBEDTLS_COMMON_MK=1 ${ATFW_OPT}
############################################

test_array=(
	h3_4x2g
	#h3_2x2g
	#h3_4x1g
	#m3
	#m3n
	#e3
	#e3_4d
	#d3
	#h3ulcb_4x2g
	#m3ulcb
	#v3u
	#s4
	#v4h
)

test_cmd=(
	 'LSI=H3 RCAR_DRAM_SPLIT=1 SPD=opteed MBEDTLS_COMMON_MK=1 RCAR_LOSSY_ENABLE=1' # H3v3
	#'LSI=H3 RCAR_DRAM_SPLIT=1 SPD=opteed MBEDTLS_COMMON_MK=1' # H3v3 Disable lossy
	#'LSI=H3 RCAR_DRAM_SPLIT=2 RCAR_DRAM_CHANNEL=5 RCAR_DRAM_LPDDR4_MEMCONF= 1 SPD=opteed MBEDTLS_COMMON_MK=1 RCAR_LOSSY_ENABLE=1'
	#'LSI=H3 RCAR_DRAM_SPLIT=1 RCAR_DRAM_LPDDR4_MEMCONF=0 SPD=opteed MBEDTLS_COMMON_MK=1 RCAR_LOSSY_ENABLE=1'
	#'LSI=M3 RCAR_DRAM_SPLIT=2 SPD=opteed MBEDTLS_COMMON_MK=1 RCAR_LOSSY_ENABLE=1'
	#'LSI=M3N SPD=opteed MBEDTLS_COMMON_MK=1 RCAR_LOSSY_ENABLE=1'
	#'LSI=E3 RCAR_SA0_SIZE=0 RCAR_AVS_SETTING_ENABLE=0 RCAR_DRAM_DDR3L_MEMCONF=0 RCAR_DRAM_DDR3L_MEMDUAL=0 SPD=opteed MBEDTLS_COMMON_MK=1'
	#'LSI=E3 RCAR_SA0_SIZE=0 RCAR_AVS_SETTING_ENABLE=0 RCAR_DRAM_DDR3L_MEMCONF=1 RCAR_DRAM_DDR3L_MEMDUAL=1 SPD=opteed MBEDTLS_COMMON_MK=1 RCAR_LOSSY_ENABLE=1'
	#'LSI=D3 RCAR_SA0_SIZE=0 RCAR_AVS_SETTING_ENABLE=0 PMIC_ROHM_BD9571=0 RCAR_SYSTEM_SUSPEND=0 DEBUG=0 SPD=opteed MBEDTLS_COMMON_MK=1'
	#'LSI=H3 RCAR_DRAM_SPLIT=1 RCAR_GEN3_ULCB=1 PMIC_LEVEL_MODE=0 SPD=opteed MBEDTLS_COMMON_MK=1 RCAR_LOSSY_ENABLE=1'
	#'LSI=M3 RCAR_DRAM_SPLIT=2 RCAR_GEN3_ULCB=1 PMIC_LEVEL_MODE=0 SPD=opteed MBEDTLS_COMMON_MK=1 RCAR_LOSSY_ENABLE=1'
	#'LSI=V3U PMIC_ROHM_BD9571=0 RCAR_SYSTEM_SUSPEND=0 AVS_SETTING_ENABLE=0 SPD=none MBEDTLS_COMMON_MK=1 CTX_INCLUDE_AARCH32_REGS=0'
	#'LSI=S4 PMIC_ROHM_BD9571=0 RCAR_SYSTEM_SUSPEND=0 AVS_SETTING_ENABLE=0 SPD=none MBEDTLS_COMMON_MK=1 CTX_INCLUDE_AARCH32_REGS=0 LOG_LEVEL=0 DEBUG=0 RCAR_BL33_EXECUTION_EL=0'
	#'LSI=V4H MBEDTLS_COMMON_MK=1 CTX_INCLUDE_AARCH32_REGS=0 LOG_LEVEL=20 DEBUG=0 ENABLE_ASSERTIONS=1 RCAR_RPC_HYPERFLASH_LOCKED=0'
)

make clean

TIMESTAMP=`date +%Y%m%d_%H%M%S`
store_log="build_${BRANCH}_log_${TIMESTAMP}.txt"

touch .scmversion

# for i in $(seq 0 0);
for i in ${!test_array[@]}
do
	echo "###### build ${test_array[$i]} ######"
	store_folder=$(pwd)/${STORE_TARGET}/${test_array[$i]}
	echo ${store_folder}
	mkdir -p ${store_folder}

	cd $ATF_HOME

	make distclean
	make bl2 bl31 rcar_layout_tool rcar_srecord LDFLAGS="" PLAT=${PLATFORM} ${test_cmd[$i]} 2>&1 | tee $store_log
	#make bl31 rcar_srecord PLAT=${PLATFORM} ${test_cmd[$i]} 2>&1 | tee $store_log #S4
	#make bl31 rcar_srecord PLAT=rcar_gen4 ${test_cmd[$i]} 2>&1 | tee $store_log #S4
	# echo ${test_cmd[$i]}


	if [ -f build/rcar/release/bl31.bin ]; then
		cp build/rcar/release/bl2.bin ${store_folder}/
		cp build/rcar/release/bl2.srec ${store_folder}/
		cp build/rcar/release/bl31.bin ${store_folder}/
		cp build/rcar/release/bl31.srec ${store_folder}/
		# cp -f build/rcar/release/bl31.srec /shsv/SS2/RSS1/23_HaiPham/test_boot/rcar-3.9.10
	else
		cp build/rcar/debug/bl2.bin ${store_folder}/
		cp build/rcar/debug/bl2.srec ${store_folder}/
		cp build/rcar/debug/bl31.bin ${store_folder}/
		cp build/rcar/debug/bl31.srec ${store_folder}/
	fi

	#cp tools/renesas/rcar_layout_create/bootparam_sa0.srec ${store_folder}/
	#cp tools/renesas/rcar_layout_create/cert_header_sa6.srec ${store_folder}/
	#cp tools/renesas/rcar_layout_create/cert_header_sa6.bin ${store_folder}/

	# mv $store_log ${store_folder}/

	echo "###### build ${test_array[$i]} DONE ######"
done