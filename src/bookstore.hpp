#pragma once

#include <string>
#include <sstream>
#include <iostream>
#include <unordered_map>

#define BOOST_BIND_GLOBAL_PLACEHOLDERS

#include <boost/foreach.hpp>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>


namespace cwt
{
    
struct book {
    std::string m_author;
    std::string m_title;

    bool operator==(const book& rhs) const {
        return  this->m_author.compare(rhs.m_author) == 0 &&
            this->m_title.compare(rhs.m_title) == 0;
    }
};

class bookstore {
    private:
        std::unordered_map<std::size_t, book> m_books;
    public:
        void add_book(std::size_t id, const book& b) {
            m_books[id] = b;
        }

        void add_books_from_json(std::stringstream& json_content) {
        
            boost::property_tree::ptree pt;
            boost::property_tree::read_json(json_content, pt);

            BOOST_FOREACH(boost::property_tree::ptree::value_type &v, pt.get_child("books")) {

                auto id = v.second.get_child("id").get_value<std::size_t>();

                book b{
                    v.second.get_child("author").get_value<std::string>(),
                    v.second.get_child("title").get_value<std::string>(),
                };    

                m_books[id] = b;  
            }
        }

        void remove_book(std::size_t id){
            m_books.erase(id);
        }
        void clear() {
            m_books.clear();
        }
        [[nodiscard]] book get_book(const std::size_t id) const {
            return m_books.at(id);
        } 
        [[nodiscard]] bool has(const book& b) {
            auto result = std::find_if(m_books.begin(), m_books.end(), [b](const auto& current){
                return b == current.second;
            });
            return result != m_books.end();
        }
        [[nodiscard]] const auto get_books() const noexcept {
            return m_books;
        }
        [[nodiscard]] std::size_t get_books_count() const noexcept {
            return m_books.size();
        }

        void print() {
            for ( auto [key, value] : m_books ) {
                std::cout << "book " << key << ": " << value.m_title << " from " << value.m_author << '\n';
            }
        }
};


} // namespace cwt
