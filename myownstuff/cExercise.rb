while(1)
{
    #define MAX_MEMBER,MAX_BOOK,MAX_TICKET, MAX_BOOK_BORROWED

    we have variable: number_of_current_member, number_of_current_book
    we have those array
    member_id
    member_name
    member_citizen_ID
    member_dayOfBirth
    member_gender
    member_email
    member_register_date
    member_expired_date (within 2 years)

    book_ISBN
    book_name 
    book_author
    book_publishing_company
    book_publishing_year
    book_type
    book_price
    book_amount -> when borrow book_amount -- ->make a malloc contain 

    lib_ticket_member_id
    lib_ticket_borrow_date
    lib_ticket_return_date_expected (max 7 days from lib_ticket_borrow_date)
    lib_ticket_return_date_real
    lib_ticket_ISBN list use pointer + malloc to point to another list contain ISBN (MAX_BOOK_BORROWED)
        lib_ticket_number_of_borrowed_book -> use to manage for loop to scan price for
    lib_ticket_is_book_exist - bool (start at true,if book is lost then turn to false )
    lib_ticket_fine (normally is 0, fine is 5000* (lib_ticket_return_date_real-lib_ticket_return_date_expected)) //mean 5000/expired day
    
    //need a function to get index from 1 array to get info from another array
    int search_index_to_get_info_fromstr(string find_this,*array[]) -> return index;
    int search_index_to_get_info_fromint(int find_this,*array[]) -> return index;

    scanf(" %d") input (case in enum):
    member_management
        show_member_list -> printf (info of member)
        add_member -> scanf to array
        delete_member -> 
    book_management
    
    borrow_book(*book_name[],*book_amount[])
        scanf(num_of_book_member_want_to_borrow)
        int* buffer = (int*)malloc(num_of_book_member_want_to_borrow*sizeof(int))
        int buffer_index = 0;
        for (int i=0;i<num_of_book_member_want_to_borrow;i++)
            scanf(book_name_request)
                if(is_book_available(book_name_request) -> check book_amount)
                    buffer[buffer_index] = book_ISBN[search_index_to_get_info_fromstr(book_name_request,book_name)]
                    buffer_index ++                    
                else
                    num_of_book_member_want_to_borrow--;
                    printf("this book cannot be borrowed");
        //set all borrowed book from index to ticket

    return_book
    statistic_analysis
}