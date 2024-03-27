#ifndef PRE_CHECK_CONFIG_PCL_H
#define PRE_CHECK_CONFIG_PCL_H

#include "pre_check_config.h"

static struct TEST_pre_check_config_Pattern pre_check_config_PCL[] =
{
	/* "Test Case ID         ",      *p_config     	   ,   DMA_API   is_stub  , image_config	square_config}, { ReturnValue ,  */
	/* pre_check_config_0001 */ { { TEST_ADDR_NOT_NULL , { E_FAILURE, TRUE   },{{0,0,0}		,	{0,0,0}		}}, { E_FAILURE    } },
	/* pre_check_config_0002 */ { { TEST_ADDR_NULL 	   , { E_SUCCESS, TRUE   },{{0,0,0}		,	{0,0,0}		}}, { E_FAILURE    } },
	/* pre_check_config_0003 */ { { TEST_ADDR_NOT_NULL , { E_SUCCESS, TRUE   },{{400,150,0}	,	{0,0,0}		}}, { E_SUCCESS    } },
	/* pre_check_config_0004 */ { { TEST_ADDR_NOT_NULL , { E_SUCCESS, TRUE   },{{0,0,0}		,	{4,2,4}		}}, { E_SUCCESS    } },
	/* pre_check_config_0005 */ { { TEST_ADDR_NOT_NULL , { E_SUCCESS, TRUE   },{{0,0,0}		,	{201,201,4}	}}, { E_SUCCESS    } },
};

#endif


