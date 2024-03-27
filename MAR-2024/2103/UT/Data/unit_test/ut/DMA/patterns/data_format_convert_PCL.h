#ifndef DATA_FORMAT_CONVERT_PCL_H
#define DATA_FORMAT_CONVERT_PCL_H

#include "data_format_convert.h"

static struct TEST_data_format_convert_Pattern data_format_convert_PCL[] =
{
	/* "Test Case ID            ", flow_encode , component  }, { ReturnValue ,  */
	/* data_format_convert_0001 */ { { 5           , 0          }, { -1           } },
	/* data_format_convert_0002 */ { { 4           , 0x3FF       }, { 0            } },
	/* data_format_convert_0003 */ { { 0           , 0x500       }, { 10.25        } }, 
	/* data_format_convert_0004 */ { { 1           , 0x500       }, { 9.75         } },
	/* data_format_convert_0005 */ { { 2           , 0x500       }, { 8.5          } },
	/* data_format_convert_0006 */ { { 3           , 0x500       }, { 7.75         } },
	/* data_format_convert_0007 */ { { 4           , 0x500       }, { 0            } },
};

#endif


