/**
 * Types and Structures
 */
typedef i64 Timestamp

struct TTodo {
    1: required i32 id,
    2: required string title,
    3: required Timestamp created_at,
}

/**
 * Exceptions
 */
enum ArgsErrorCode {
    UNKNOWN_ERROR = 0,
    DATABASE_ERROR = 1,
    TOO_BUSY_ERROR = 2,
}

exception ArgsUserException {
   1: required ArgsErrorCode error_code,
   2: required string error_name,
   3: optional string message,
}

exception ArgsSystemException {
   1: required ArgsErrorCode error_code,
   2: required string error_name,
   3: optional string message,
}

exception ArgsUnknownException {
   1: required ArgsErrorCode error_code,
   2: required string error_name,
   3: required string message,
}

/**
 * API
 */
service ArgsService {
    bool ping()
        throws (1: ArgsUserException user_exception,
                2: ArgsSystemException system_exception,
                3: ArgsUnknownException unknown_exception,)

    bool yay(1:i32 id)
        throws (1: ArgsUserException user_exception,
                2: ArgsSystemException system_exception,
                3: ArgsUnknownException unknown_exception,)

    bool nay(1:i32 id)
        throws (1: ArgsUserException user_exception,
                2: ArgsSystemException system_exception,
                3: ArgsUnknownException unknown_exception,)

    list<TTodo> list_todo()
        throws (1: ArgsUserException user_exception,
                2: ArgsSystemException system_exception,
                3: ArgsUnknownException unknown_exception,)

    void add_todo(1:string title)
        throws (1: ArgsUserException user_exception,
                2: ArgsSystemException system_exception,
                3: ArgsUnknownException unknown_exception,)

    void complete_todo(1:i32 id)
        throws (1: ArgsUserException user_exception,
                2: ArgsSystemException system_exception,
                3: ArgsUnknownException unknown_exception,)

    void counters_init()
        throws (1: ArgsUserException user_exception,
                2: ArgsSystemException system_exception,
                3: ArgsUnknownException unknown_exception,)
        
    string get_counters()
        throws (1: ArgsUserException user_exception,
                2: ArgsSystemException system_exception,
                3: ArgsUnknownException unknown_exception,)

    string fusion_alt(1:i32 num)
        throws (1: ArgsUserException user_exception,
                2: ArgsSystemException system_exception,
                3: ArgsUnknownException unknown_exception,)

    string fusion_test(1:i32 num)
        throws (1: ArgsUserException user_exception,
                2: ArgsSystemException system_exception,
                3: ArgsUnknownException unknown_exception,)

    void signal(1:i32 num)
        throws (1: ArgsUserException user_exception,
                2: ArgsSystemException system_exception,
                3: ArgsUnknownException unknown_exception,)
}
