import csv
import os
import time
import asyncio
import pandas as pd
from random import randint
from datetime import datetime
from twikit import Client, TooManyRequests
from langdetect import detect, LangDetectException
from deep_translator import GoogleTranslator
from deep_translator.exceptions import TranslationNotFound

async def twitter_scrapper(cookies: str | None = None,
               user_info1: str | None = None,
               user_info2: str | None = None,
               password: str | None = None,
               tcount : int = 10, 
               q : str = 'gemini AI'):

    count = 0
    results = {}
    tweet_id = []
    tweet_text = []
    tweet_hashtag = []
    tweet_timestamp = []

    client = Client()
    start_time = time.time()
    if cookies is None:
        try:
            await client.login(
                auth_info_1= user_info1,
                auth_info_2= user_info2,
                password= password,
                cookies_file= "cookies.json"
            )
        except Exception as e:
            print("Terjadi Eror, Silahkan lihat informasi di bawah ini..")
            print("--" * 25)
            print(e)
            print("--" * 25)
    else:
        try:
            client.load_cookies(cookies)
        except Exception as e:
            print("Terjadi Eror, Silahkan lihat informasi di bawah ini..")
            print("--" * 25)
            print(e)
            print("--" * 25)

    query_results = None
    while count < tcount:
        if query_results is None:
            print(f"[LOG : {datetime.now()}] Mulai Mencari Tweet...")
            try:
                query_results = await client.search_tweet(query=q, product="Top")
            except TooManyRequests as e:
                rate_limit = datetime.fromtimestamp(e.rate_limit_reset)
                print(f"[LOG : {datetime.now()}] Rate Limit, Mohon tunggu selama {rate_limit}")
                wait_limit = max(0, (rate_limit - datetime.now()).total_seconds())
                await asyncio.sleep(wait_limit)
                continue
        else:
            sleep_t = randint(5, 10)
            print(f"[LOG : {datetime.now()}] {count} Total Tweet ditemukan")
            print(f"[LOG : {datetime.now()}] Mencari Tweet Selanjutnya dalam {sleep_t} Detik...")
            await asyncio.sleep(sleep_t)
            try : 
                query_results = await query_results.next()
            except TooManyRequests as e:
                rate_limit = datetime.fromtimestamp(e.rate_limit_reset)
                print(f"[LOG : {datetime.now()}] Rate Limit, Mohon tunggu hingga {rate_limit}")
                wait_limit = max(0, (rate_limit - datetime.now()).total_seconds())
                await asyncio.sleep(wait_limit)
                continue

        if not query_results:
            print(f"[LOG : {datetime.now()}] Tidak Ada Tweet yang tersisa")
            break

        for result in query_results:
            count += 1
            tweet_id.append(result.id)
            tweet_text.append(result.text)
            tweet_timestamp.append(result.created_at_datetime)
            if result.hashtags is None:
                tweet_hashtag.append("No HashTag")
            else:
                hashtag_str = ", ".join(result.hashtags)
                tweet_hashtag.append(hashtag_str)

    results["Tweet ID"] = tweet_id
    results["Tweet Time Stamp"] = tweet_timestamp
    results["Tweet Text"] = tweet_text
    results["Tweet Hashtag"] = tweet_hashtag

    stop_time = time.time()
    time_process_sec = stop_time - start_time
    jam = int(time_process_sec // 3600)
    menit = int((time_process_sec % 3600) // 60)
    detik = int(time_process_sec % 60)
    await asyncio.sleep(1.2)
    print(f"[LOG : {datetime.now()}] Target terpenuhi!!")
    await asyncio.sleep(1.2)
    print(f"[LOG : {datetime.now()}] {count} Tweet ditemukan")
    await asyncio.sleep(1.2)
    print(f"[LOG : {datetime.now()}] Waktu Proses {jam}:{menit}:{detik}")
    for i in reversed(range(1,6)):
        print(f"[LOG : {datetime.now()}] Menutup Program dalam {i}")
        await asyncio.sleep(1.2)
    print(f"[LOG : {datetime.now()}] Terimakasih :)")

    return results

def text_translator(text_list: list | str):
    translator = GoogleTranslator(source="auto", target="en")
    result = []
    # cek apakah text adalah sebuah string atau hanya text biasa
    if type(text_list) is list:
        for text in text_list:
            try:
                language = detect(text)
                translator.source = language
                text_translated = translator.translate(text) if language != "en" else text
                result.append(text_translated)
            except (LangDetectException, TranslationNotFound):
                result.append(text)
                continue
    else:
        try:
            language = detect(text_list)
            translator.source = language
            text_translated = translator.translate(text_list) if language != "en" else text_list
            return text_translated
        except (LangDetectException, TranslationNotFound):
            return text_list   

    return result

async def main(query_search, tweets_csv_file, cookies, count, user_name = None, password = None, email = None):
    # Memuat file query
    with open(query_search) as file:
        heading = next(file) # tidak mengambil nama kolom
        queries = csv.reader(file)
        for idx, query in enumerate(queries):
            print(f"Mencoba query ke-{idx}")
            # mengambil text query
            query_to_search = query[0]
            # cek apakah user info di masukan atau tidak jika tidak maka akses menggunakan cookies
            if password and (user_name or email): 
                query_result = await twitter_scrapper(user_info1=user_name, user_info2=email, password=password, tcount=count, q=query_to_search)
            else:
                query_result = await twitter_scrapper(cookies=cookies, tcount=count, q=query_to_search)
            # Konversi ke DataFrame
            df = pd.DataFrame(query_result)
            # Membuat kolom untuk text yang sudah di terjemahkan
            df["Tweet Translated"] = df["Tweet Text"].apply(text_translator)
            # Cek apakah file csv ada dalam direktori atau tidak
            if not os.path.exists(tweets_csv_file):
                # jika belum ada maka akan membuat file baru
                df.to_csv(tweets_csv_file, index=False)
            else:
                # jika file ada maka sisipkan hasilnya
                df.to_csv(tweets_csv_file, mode='a', header=False, index=False)
            
if __name__ == "__main__":
    # Inisialisasi Variabel yang dibutuhkan
    csv_file = "tweets_data.csv"
    twitter_query_file = "query.csv"
    cookies = "cookies.json"
    q_count_result = 10000
    # Eksekusi Fungsi Main()
    asyncio.run(main(
        query_search= twitter_query_file,
        tweets_csv_file= csv_file,
        cookies= cookies,
        count= q_count_result
    ))




