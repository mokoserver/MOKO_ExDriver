#include "extcode.h"
#pragma pack(push)
#pragma pack(1)

#ifdef __cplusplus
extern "C" {
#endif
typedef struct {
	LVBoolean status;
	int32_t code;
	LStrHandle source;
	} TD1;


/*!
 * json
 */
void __cdecl json(char Command[], TD1 *errorIn, char Response[], 
	TD1 *errorOut, int32_t len);

MgErr __cdecl LVDLLStatus(char *errStr, int errStrLen, void *module);

void __cdecl SetExcursionFreeExecutionSetting(Bool32 value);

#ifdef __cplusplus
} // extern "C"
#endif

#pragma pack(pop)

