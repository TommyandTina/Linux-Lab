#ifndef DMA_API_PCL_H
#define DMA_API_PCL_H

#include "DMA_API.h"

static struct TEST_DMA_API_Pattern DMA_API_PCL[] =
{
	/* "Test Case ID", 	   x  , y , *p_dma_config      , offset_x , offset_y , width , height , enable , exclude  }, { ReturnValue          , *p_dma_config      , offset_x , offset_y , width , height , enable , exclude , validator , validator , validator , validator , validator , validator , validator  } */
	/* DMA_API_0001 */ { { 0  , 0 , TEST_ADDR_NULL     , { 0      , 0        , 0     , 0      , TRUE   , TRUE }   }, { E_VALIDATION_FAILURE , 0                  , { 0      , 0        , 0     , 0      , 0      , 0 }      }, { FALSE     , FALSE     , FALSE     , FALSE     , FALSE     , FALSE     , FALSE      } },
	/* DMA_API_0002 */ { { 0  , 0 , TEST_ADDR_NOT_NULL , { 0      , 0        , 0     , 0      , FALSE  , TRUE }   }, { E_SUCCESS            , TEST_ADDR_NOT_NULL , { 0      , 0        , 0     , 0      , FALSE  , TRUE }   }, { TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE       } },
	/* DMA_API_0003 */ { { 0  , 0 , TEST_ADDR_NOT_NULL , { 1      , 0        , 0     , 0      , TRUE   , TRUE }   }, { E_SUCCESS            , TEST_ADDR_NOT_NULL , { 1      , 0        , 0     , 0      , TRUE   , TRUE }   }, { TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE       } },
	/* DMA_API_0004 */ { { 0  , 0 , TEST_ADDR_NOT_NULL , { 0      , 1        , 0     , 0      , TRUE   , TRUE }   }, { E_SUCCESS            , TEST_ADDR_NOT_NULL , { 0      , 1        , 0     , 0      , TRUE   , TRUE }   }, { TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE       } },
	/* DMA_API_0005 */ { { 2  , 0 , TEST_ADDR_NOT_NULL , { 0      , 0        , 2     , 0      , TRUE   , TRUE }   }, { E_SUCCESS            , TEST_ADDR_NOT_NULL , { 0      , 0        , 2     , 0      , TRUE   , TRUE }   }, { TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE       } },
	/* DMA_API_0006 */ { { 0  , 2 , TEST_ADDR_NOT_NULL , { 0      , 0        , 0     , 2      , TRUE   , TRUE }   }, { E_SUCCESS            , TEST_ADDR_NOT_NULL , { 0      , 0        , 0     , 2      , TRUE   , TRUE }   }, { TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE       } },
	/* DMA_API_0007 */ { { 0  , 0 , TEST_ADDR_NOT_NULL , { 1      , 0        , 0     , 0      , TRUE   , FALSE }  }, { E_FAILURE            , TEST_ADDR_NOT_NULL , { 1      , 0        , 0     , 0      , TRUE   , FALSE }  }, { TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE       } },
	/* DMA_API_0008 */ { { 15 , 9 , TEST_ADDR_NOT_NULL , { 1      , 1        , 16    , 10     , TRUE   , TRUE }   }, { E_FAILURE            , TEST_ADDR_NOT_NULL , { 1      , 1        , 16    , 10     , TRUE   , TRUE }   }, { TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE       } },
	/* DMA_API_0009 */ { { 15 , 9 , TEST_ADDR_NOT_NULL , { 1      , 1        , 16    , 10     , TRUE   , FALSE }  }, { E_SUCCESS            , TEST_ADDR_NOT_NULL , { 1      , 1        , 16    , 10     , TRUE   , FALSE }  }, { TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE       } },
	// /* DMA_API_0010 */ { { 15 , 9 , TEST_ADDR_NOT_NULL , { 1      , 1        , 16    , 10     , TRUE   , FALSE }  }, { E_SUCCESS            , TEST_ADDR_NOT_NULL , { 1      , 1        , 16    , 10     , TRUE   , FALSE }  }, { TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE      , TRUE       } }
};

#endif


