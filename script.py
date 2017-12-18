#                                                                              #
#                                                         :::      ::::::::    #
#    script.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ssabbah <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/18 15:17:26 by ssabbah           #+#    #+#              #
#    Updated: 2017/12/18 15:52:05 by ssabbah          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import embeddings
#
# emb = embeddings.EmbeddingsDictionary (100000)
# geek = emb.embed("geek")
# neighbors = emb.emb2neighbors(geek)
# for i in neighbors[1]:
#        print(emb.words[i])

e=embeddings.EmbeddingsDictionary(250000)
e.analogy('sea', 'bird', 'fish')
