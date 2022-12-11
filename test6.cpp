#include <stdio.h>
#include <unistd.h>
#include "uthread.h"

void long_thread(void* arg)
{
    usleep(1000000);
    uthread_exit();
}

void thread1(void* arg)
{
    void* stack = NULL;
    __asm__ __volatile__("mov %%rsp, %0" : "=r"(stack) :: "memory");
    printf("stack for thread 1: %p\n", stack);
    for (int i = 0; i < 10; i++) {
        __asm__ __volatile__("mov %%rsp, %0" : "=r"(stack) :: "memory");
        printf("stack for thread 1: %p\n", stack);
        uthread_yield();
    }
    uthread_exit();
}

void thread2(void* arg)
{
    void* stack = NULL;
    __asm__ __volatile__("mov %%rsp, %0" : "=r"(stack) :: "memory");
    printf("stack for thread 2: %p\n", stack);
    for (int i = 0; i < 10; i++) {
        __asm__ __volatile__("mov %%rsp, %0" : "=r"(stack) :: "memory");
        printf("stack for thread 2: %p\n", stack);
        uthread_yield();
    }
    uthread_exit();
}

int main(int argc, const char** argv)
{
    uthread_set_policy(UTHREAD_PRIORITY);
    uthread_init();
    uthread_create(long_thread, NULL);
    uthread_create(long_thread, NULL);
    uthread_create(long_thread, NULL);
    uthread_create(thread1, NULL);
    uthread_create(thread2, NULL);
    uthread_cleanup();
    return 0;
}
