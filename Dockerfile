FROM ubuntu
RUN apt-get update && apt-get install -y iputils-ping
# توحيد الأسماء لتكون واضحة
ENV PROG=ping
ENV TARGET=8.8.8.8
# استدعاء نفس الأسماء التي عرفتها أعلاه
CMD ${PROG} ${TARGET}

