#ifndef PRE_CHECK_CONFIG_PCL_H
#define PRE_CHECK_CONFIG_PCL_H

#include "pre_check_config.h"

static struct TEST_pre_check_config_Pattern pre_check_config_PCL[] =
{
	/* "Test Case ID         ", *p_config          , DMA_API              }, { ReturnValue ,  */
	/* pre_check_config_0001 */ { { TEST_ADDR_NOT_NULL , { E_FAILURE, TRUE }  }, { E_FAILURE    } }
};

#endif


